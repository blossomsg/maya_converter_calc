# modules_for_ui
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class MayaConverterCalcUI(QtWidgets.QWidget):
	"""This Class is UI for converting metric to cm in maya

		Attributes:

		"""

	def __init__(self):
		super(MayaConverterCalcUI, self).__init__()

		# CAVEAT : Parent the UI to the application Maya
		self.setParent(ptr_instance)
		self.setWindowFlags(QtCore.Qt.Window)

		# CAVEAT : Value box and dropdown to choose type of metric
		self.mcc_value_box_qlineedit = QtWidgets.QLineEdit()
		self.validator = QtGui.QDoubleValidator(0.0, 999.0, 3)
		self.mcc_value_box_qlineedit.setValidator(self.validator)
		self.mcc_metric_dropdown_combobox = QtWidgets.QComboBox()
		self.mcc_metric_dropdown_inch = self.mcc_metric_dropdown_combobox.addItem("inch")
		self.mcc_metric_dropdown_foot = self.mcc_metric_dropdown_combobox.addItem("foot")
		self.mcc_metric_dropdown_metre = self.mcc_metric_dropdown_combobox.addItem("metre")
		self.mcc_result_qlineedit = QtWidgets.QLineEdit()
		self.mcc_result_qlineedit.setReadOnly(True)
		self.mcc_calculate_qpushbutton = QtWidgets.QPushButton("Calculate")

		# CAVEAT : Layouts
		self.mcc_value_and_metric_hlayout = QtWidgets.QHBoxLayout()  # horizontal layout
		self.mcc_vlayout = QtWidgets.QVBoxLayout()  # vertical layout

		# CAVEAT : Adding widgets to layouts
		self.mcc_value_and_metric_hlayout.addWidget(self.mcc_value_box_qlineedit)
		self.mcc_value_and_metric_hlayout.addWidget(self.mcc_metric_dropdown_combobox)
		self.mcc_vlayout.addLayout(self.mcc_value_and_metric_hlayout)
		self.mcc_vlayout.addWidget(self.mcc_result_qlineedit)
		self.mcc_vlayout.addWidget(self.mcc_calculate_qpushbutton)

		# CAVEAT : UI additional details
		self.setLayout(self.mcc_vlayout)
		self.setWindowTitle("MCC v1.0")
		# self.setWindowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
		# self.windowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
		self.setFixedSize(300, 100)


if __name__ == "__main__":
	print "This is Main MayaConverterCalcUI"
else:
	print "This is MayaConverterCalcUI"


# import sys
# #maya_converter_calc_ui.py
# #maya_converter_calc_func.py
# path = "D:\\All_Projs\\amazon_proj\\"
# if path in sys.path:
#     print "path already exists"
# else:
#     print "path does not exist"
#     sys.path.append(path)
#
# import maya_converter_calc_func
# import maya_converter_calc_ui
# reload(maya_converter_calc_func)
# reload(maya_converter_calc_ui)
# window = maya_converter_calc_func.MayaConverterCalcFunc()
# window = maya_converter_calc_ui.MayaConverterCalcUI()
# window.show()