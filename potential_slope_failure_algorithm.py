# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Processing Potential Slope Failure
                                 A QGIS plugin
 Potential Slope Failure for processing toolbox
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-02-01
        copyright            : (C) 2021 by Fredrik Lindberg
        email                : fredrikl@gvc.gu.se
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Fredrik Lindberg'
__date__ = '2020-02-01'
__copyright__ = '(C) 2021 by Fredrik Lindberg'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication, QDate, QTime, Qt, QVariant
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterString,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFolderDestination,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingException,
                    #    QgsProcessingParameterPoint,
                       QgsProcessingParameterRasterLayer)
from processing.gui.wrappers import WidgetWrapper
from qgis.PyQt.QtWidgets import QDateEdit, QTimeEdit, QMessageBox
from qgis.PyQt.QtGui import QIcon
from osgeo import gdal, osr
from osgeo.gdalconst import *
import os
import inspect
from pathlib import Path
import webbrowser
import numpy as np

from . import shadowingfunctions as shadow

# import matplotlib.pyplot as plt

class ProcessingPotentialSlopeFailureAlgorithm(QgsProcessingAlgorithm):
    """
    This algorithm is a processing version of PotentialSlopeFailure
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.
    INPUT_DEM = 'INPUT_DEM'
    INPUT_SOIL = 'INPUT_SOIL'
    SEARCH_DIR = 'SEARCH_DIR'
    SLOPE_ANGLE = 'SLOPE_ANGLE'
    OUTPUT_RASTER = 'OUTPUT_RASTER'
    #OUTPUT_DIR = 'OUTPUT_DIR'
    # EXTENT = 'EXTENT'

    def initAlgorithm(self, config):
        # self.addParameter(QgsProcessingParameterPoint(self.EXTENT,
        #         self.tr('Extent'), None, False))
        # self.addParameter(QgsProcessingParameterExtent(self.EXTENT,
        #         self.tr('Extent'), None, False))
        self.addParameter(QgsProcessingParameterRasterLayer(self.INPUT_DEM,
                self.tr('Digital Elevation Model (DEM)'), None, False))
        self.addParameter(QgsProcessingParameterRasterLayer(self.INPUT_SOIL,
                self.tr('Cohesive soils (1 = Cohesive soil, 0 = Other'), None, False))
        self.addParameter(QgsProcessingParameterNumber(self.SEARCH_DIR, 
            self.tr('Number of search directions:'), 
            QgsProcessingParameterNumber.Integer,
            QVariant(16), True, minValue=0, maxValue=100))
        self.addParameter(QgsProcessingParameterNumber(self.SLOPE_ANGLE, 
            self.tr('Slope failure angle:'), 
            QgsProcessingParameterNumber.Double,
            QVariant(10), True, minValue=0, maxValue=100))
        self.addParameter(QgsProcessingParameterRasterDestination(self.OUTPUT_RASTER,
            self.tr("Output raster file"),
            None, False))
        #self.addParameter(QgsProcessingParameterFolderDestination(self.OUTPUT_DIR,
        #                                             'Output folder'))


    def processAlgorithm(self, parameters, context, feedback):
        # InputParameters
        # Load DEM
        demlayer = self.parameterAsRasterLayer(parameters, self.INPUT_DEM, context)
        # Load soil layer
        soillayer = self.parameterAsRasterLayer(parameters, self.INPUT_SOIL, context)
        # Number of search directions
        search_dir = self.parameterAsInt(parameters, self.SEARCH_DIR, context)
        # Slope failure angle
        slope_angle = self.parameterAsDouble(parameters, self.SLOPE_ANGLE, context)
        # Output raster file
        outputRaster = self.parameterAsOutputLayer(parameters, self.OUTPUT_RASTER, context)
        # Output directory
        # outputDir = self.parameterAsString(parameters, self.OUTPUT_DIR, context)

        if parameters['OUTPUT_RASTER'] == 'TEMPORARY_OUTPUT':
            if not (os.path.isdir(outputRaster)):
                os.mkdir(outputRaster)

        if demlayer is None:
            raise QgsProcessingException('Error! No valid DEM raster selected.')
        #    QMessageBox.critical(None, "Error", "No valid DEM raster layer is selected")
        #    return

        provider = demlayer.dataProvider()
        filepath_dem = str(provider.dataSourceUri())

        gdal_dem = gdal.Open(filepath_dem)

        dem = gdal_dem.ReadAsArray().astype(float)
        sizex = dem.shape[0]
        sizey = dem.shape[1]

        geotransform = gdal_dem.GetGeoTransform()
        scale = 1 / geotransform[1]

        if soillayer is None:
            raise QgsProcessingException('Error! No valid Soil raster selected.')
        #    QMessageBox.critical(None, "Error", "No valid Soil raster selected")
        #    return

        # load soil raster
        gdal.AllRegister()
        provider = soillayer.dataProvider()
        filePathOld = str(provider.dataSourceUri())
        dataSet = gdal.Open(filePathOld)
        soil = dataSet.ReadAsArray().astype(float)

        soilsizex = soil.shape[0]
        soilsizey = soil.shape[1]

        if not (soilsizex == sizex) & (soilsizey == sizey):
            raise QgsProcessingException('Error! The grids must be of same extent and resolution')
            #print("The grids must be of same extent and resolution")
            # QMessageBox.critical(None, "Error", "The grids must be of same extent and resolution")
            return

        itera = int(360 / search_dir)
        alt = slope_angle
        shtot = np.zeros((sizex, sizey))
        index = 0

        # Inverting dem
        dem = dem * (-1.) + np.max(dem)

        for i in range(0, search_dir):
            if feedback.isCanceled():
                break

            azi = itera * i
            feedback.setProgressText("Running search direction " + str(index) + " of " + str(search_dir) + "...")
            sh = shadow.shadowingfunctionglobalradiation(dem, azi, alt, scale, feedback, 0)
            shtot = shtot + sh
            index += 1
            feedback.setProgressText("Search direction " + str(index) + " of " + str(search_dir) + " finished...")

        zon1 = shtot / index

        zon1[zon1 == 1] = 2
        zon1[zon1 < 1] = 1
        karta1a = zon1 * soil
        karta1a[karta1a == 0] = 3

        self.saveraster(gdal_dem, outputRaster, karta1a)

        #filename = self.folderPath[0] + '/map1a.tif'
        #self.saveraster(gdal_dem, filename, karta1a)

        # load result into canvas
##        if self.dlg.checkBoxIntoCanvas.isChecked():
##            rlayer = self.iface.addRasterLayer(filename)
##
##            # Trigger a repaint
##            if hasattr(rlayer, "setCacheImage"):
##                rlayer.setCacheImage(None)
##            rlayer.triggerRepaint()
##
##            rlayer.loadNamedStyle(self.plugin_dir + '/misc/map1a.qml')
##
##            if hasattr(rlayer, "setCacheImage"):
##                rlayer.setCacheImage(None)
##            rlayer.triggerRepaint()
##
##        self.dlg.progressBar.setValue(0)
##
##        QMessageBox.information(self.dlg, "Calculation done!", "Output (map1a.tif) created in: " + self.folderPath[0] + "/")

        

        feedback.setProgressText("Potential Slope Failure grid successfully generated")

        return {self.OUTPUT_RASTER: outputRaster}
    
    def saveraster(self, gdal_data, filename, raster):
        rows = gdal_data.RasterYSize
        cols = gdal_data.RasterXSize

        outDs = gdal.GetDriverByName("GTiff").Create(filename, cols, rows, int(1), GDT_Float32)
        outBand = outDs.GetRasterBand(1)

        # write the data
        outBand.WriteArray(raster, 0, 0)
        # flush data to disk, set the NoData value and calculate stats
        outBand.FlushCache()
        outBand.SetNoDataValue(-9999)

        # georeference the image and set the projection
        outDs.SetGeoTransform(gdal_data.GetGeoTransform())
        outDs.SetProjection(gdal_data.GetProjection())

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Potential Slope Failure'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    # def group(self):
    #     """
    #     Returns the name of the group this algorithm belongs to. This string
    #     should be localised.
    #     """
    #     return self.tr(self.groupId())

    # def groupId(self):
    #     """
    #     Returns the unique ID of the group this algorithm belongs to. This
    #     string should be fixed for the algorithm, and must not be localised.
    #     The group id should be unique within each provider. Group id should
    #     contain lowercase alphanumeric characters only and no spaces or other
    #     formatting characters.
    #     """
    #     return 'Processor'

    def shortHelpString(self):
        return self.tr(
            '''

This QGIS plugin presents a method using shadow casting algorithms for preliminary landslide susceptibility mapping in cohesive soils. The result outcome maps out areas prone to slope failure in cohesive soils based on three classes:

    Zone I, spontaneous landslides could occur
    Zone II, no spontaneous landslide can occur but are adjacent to a Zone I area
    Zone III, no landslides can occur.

The method is explained in detail in Lindberg et al. (2011). http://www.sciencedirect.com/science/article/pii/S0266352X11000693

Two sets of input data are required:

    A Digital Elevation model (raster)
    A Boolean raster where 0 = no cohesive soils and 1 = cohesive soils.

    Both raster datasets must be of same size and extent.

Two additional settings can be made:

    Number of search directions.
    Slope failure angle.
'''
)

    def helpUrl(self):
        url = "https://github.com/biglimp/PotentialSlopeFailure/wiki/Potential-Slope-Failure-plugin-for-QGIS"
        return url

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def icon(self):
        cmd_folder = Path(os.path.split(inspect.getfile(inspect.currentframe()))[0]).parent
        icon = QIcon(str(cmd_folder) + "/icons/icon.png")
        return icon

    def createInstance(self):
        return ProcessingPotentialSlopeFailureAlgorithm()
