#!/usr/bin/python3
from pydm import Display
from pydm.widgets.related_display_button import PyDMRelatedDisplayButton
from pydm.widgets.label import PyDMLabel

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont

dipole = [
    'SI-Reg:PS-B12-1_1A',
    'SI-Reg:PS-B12-1_1B',
    'SI-Reg:PS-B12-1_2A',
    'SI-Reg:PS-B12-1_2B',
    'SI-Reg:PS-B12-1_3A',
    'SI-Reg:PS-B12-1_3B',
    'SI-Reg:PS-B12-1_4A',
    'SI-Reg:PS-B12-1_4B',
    'SI-Reg:PS-B12-2_1A',
    'SI-Reg:PS-B12-2_1B',
    'SI-Reg:PS-B12-2_2A',
    'SI-Reg:PS-B12-2_2B',
    'SI-Reg:PS-B12-2_3A',
    'SI-Reg:PS-B12-2_3B',
    'SI-Reg:PS-B12-2_4A',
    'SI-Reg:PS-B12-2_4B',
]
quadrupole = [
    'SI-Reg:PS-QFAP',
    'SI-Reg:PS-QFB',
    'SI-Reg:PS-QDAP12',
    'SI-Reg:PS-QDB12',
    'SI-Reg:PS-Q12_A',
    'SI-Reg:PS-Q12_B',
    'SI-Reg:PS-Q12_C',
    'SI-Reg:PS-Q33_A',
    'SI-Reg:PS-Q33_B',
    'SI-Reg:PS-Q33_C',
]
sextupole = [
    'SI-Reg:PS-SDAP0',
    'SI-Reg:PS-SDB0',
    'SI-Reg:PS-SFAP0',
    'SI-Reg:PS-SFB0',
    'SI-Reg:PS-SDB1',
    'SI-Reg:PS-SDA12',
    'SI-Reg:PS-SDA3FA1',
    'SI-Reg:PS-SDB2',
    'SI-Reg:PS-SFA2DP1',
    'SI-Reg:PS-SDB3',
    'SI-Reg:PS-SDP23',
    'SI-Reg:PS-SFB1',
    'SI-Reg:PS-SFP12',
    'SI-Reg:PS-SFB2'
]


def get_overview_detail(name):
    overview = PyDMRelatedDisplayButton('Overview')
    overview.macros = ['{"P":"' + name + '"}']
    overview.filenames = ['simple.ui']
    overview.openInNewWindow = True
    overview.showIcon = False

    detail = PyDMRelatedDisplayButton('Details')
    detail.macros = ['{"P":"' + name + '"}']
    detail.filenames = ['main.ui']
    detail.openInNewWindow = True
    detail.showIcon = False

    return overview, detail


class Launcher(Display):
    def __init__(self, parent=None, macros=None, **kwargs):
        super().__init__(parent=parent, ui_filename='launch.ui')

        grid_layout = QGridLayout()
        self.scrollAreaWidgetContents.setLayout(grid_layout)

        category_font = QFont()
        category_font.setBold(True)

        i = 0
        lbl = QLabel('Dipoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1

        for name in dipole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1

        lbl = QLabel('Quadrupoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1
        for name in quadrupole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1

        lbl = QLabel('Sextupoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1
        for name in sextupole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1
