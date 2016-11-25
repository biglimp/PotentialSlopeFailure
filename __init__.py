# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PotentialSlopeFailure
                                 A QGIS plugin
 This plugin maps potential slope failures in cohesive soils
                             -------------------
        begin                : 2016-11-25
        copyright            : (C) 2016 by Fredrik Lindberg, Gothenburg University
        email                : fredrikl@gvc.gu.se
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PotentialSlopeFailure class from file PotentialSlopeFailure.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .psf import PotentialSlopeFailure
    return PotentialSlopeFailure(iface)
