# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PotentialSlopeFailure
                                 A QGIS plugin
 This plugin maps potential slope failures in cohesive soils
                              -------------------
        begin                : 2016-11-25
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Fredrik Lindberg, Gothenburg University
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from psf_dialog import PotentialSlopeFailureDialog
import os.path
#from misc import *
import webbrowser
from osgeo import gdal
import numpy as np
import shadowingfunctions as shadow
from osgeo.gdalconst import *


class PotentialSlopeFailure:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'PotentialSlopeFailure_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = PotentialSlopeFailureDialog()
        self.dlg.runButton.clicked.connect(self.start_progress)
        self.dlg.pushButtonHelp.clicked.connect(self.help)
        self.dlg.pushButtonSave.clicked.connect(self.folder_path)
        self.fileDialog = QFileDialog()
        self.fileDialog.setFileMode(4)
        self.fileDialog.setAcceptMode(1)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Potential Slope Failure')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'PotentialSlopeFailure')
        self.toolbar.setObjectName(u'PotentialSlopeFailure')

        # self.layerComboManagerDEM = RasterLayerCombo(self.dlg.comboBoxDem)
        # RasterLayerCombo(self.dlg.comboBoxDem, initLayer="")
        # self.layerComboManagerSOIL = RasterLayerCombo(self.dlg.comboBoxSoil)
        # RasterLayerCombo(self.dlg.comboBoxSoil, initLayer="")
        self.layerComboManagerDEM = QgsMapLayerComboBox(self.dlg.widgetDEM)
        self.layerComboManagerDEM.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.layerComboManagerDEM.setFixedWidth(175)
        self.layerComboManagerSOIL = QgsMapLayerComboBox(self.dlg.widgetSOIL)
        self.layerComboManagerSOIL.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.layerComboManagerSOIL.setFixedWidth(175)
        self.folderPath = 'None'

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('PotentialSlopeFailure', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        # self.dlg = PotentialSlopeFailureDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/PotentialSlopeFailure/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Calculates areas prone to slope failures in cohesive soils'),
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Potential Slope Failure'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def folder_path(self):
        self.fileDialog.open()
        result = self.fileDialog.exec_()
        if result == 1:
            self.folderPath = self.fileDialog.selectedFiles()
            self.dlg.textOutput.setText(self.folderPath[0])

    def start_progress(self):
        if self.folderPath == 'None':
            QMessageBox.critical(None, "Error", "Select a valid output folder")
            return

        # Load DEM
        demlayer = self.layerComboManagerDEM.currentLayer()

        if demlayer is None:
            QMessageBox.critical(None, "Error", "No valid DEM raster layer is selected")
            return

        provider = demlayer.dataProvider()
        filepath_dem = str(provider.dataSourceUri())

        gdal_dem = gdal.Open(filepath_dem)

        dem = gdal_dem.ReadAsArray().astype(np.float)
        sizex = dem.shape[0]
        sizey = dem.shape[1]

        geotransform = gdal_dem.GetGeoTransform()
        scale = 1 / geotransform[1]

        # Load Soil
        soillayer = self.layerComboManagerSOIL.currentLayer()

        if soillayer is None:
            QMessageBox.critical(None, "Error", "No valid Soil raster selected")
            return

        # load raster
        gdal.AllRegister()
        provider = soillayer.dataProvider()
        filePathOld = str(provider.dataSourceUri())
        dataSet = gdal.Open(filePathOld)
        soil = dataSet.ReadAsArray().astype(np.float)

        soilsizex = soil.shape[0]
        soilsizey = soil.shape[1]

        if not (soilsizex == sizex) & (soilsizey == sizey):
            QMessageBox.critical(None, "Error", "The grids must be of same extent and resolution")
            return

        itera = int(360 / self.dlg.spinBoxIter.value())
        alt = self.dlg.spinBoxAlt.value()
        shtot = np.zeros((sizex, sizey))
        index = 0

        # Inverting dem
        dem = dem * (-1.) + np.max(dem)

        self.dlg.progressBar.setRange(0, self.dlg.spinBoxIter.value())

        for i in range(0, self.dlg.spinBoxIter.value()):
            azi = itera * i
            self.dlg.progressBar.setValue(i + 1)
            # self.iface.messageBar().pushMessage("ShadowGenerator", str(azi))
            sh = shadow.shadowingfunctionglobalradiation(dem, azi, alt, scale, self.dlg, 1)
            shtot = shtot + sh
            index += 1

        zon1 = shtot / index

        zon1[zon1 == 1] = 2
        zon1[zon1 < 1] = 1
        karta1a = zon1 * soil
        karta1a[karta1a == 0] = 3

        filename = self.folderPath[0] + '/map1a.tif'
        self.saveraster(gdal_dem, filename, karta1a)

        # load result into canvas
        if self.dlg.checkBoxIntoCanvas.isChecked():
            rlayer = self.iface.addRasterLayer(filename)

            # Trigger a repaint
            if hasattr(rlayer, "setCacheImage"):
                rlayer.setCacheImage(None)
            rlayer.triggerRepaint()

            rlayer.loadNamedStyle(self.plugin_dir + '/misc/map1a.qml')

            if hasattr(rlayer, "setCacheImage"):
                rlayer.setCacheImage(None)
            rlayer.triggerRepaint()

        self.dlg.progressBar.setValue(0)

    def help(self):
        url = "https://github.com/biglimp/PotentialSlopeFailure/wiki/Potential-Slope-Failure-plugin-for-QGIS"
        webbrowser.open_new_tab(url)

    def run(self):
        self.dlg.show()
        self.dlg.exec_()

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
