# modules_for_ui_func
import maya_converter_calc_ui


class MayaConverterCalcFunc(maya_converter_calc_ui.MayaConverterCalcUI):
	"""This Class is Func for UI converting metric to cm in maya

		Attributes:

		"""

	def __init__(self):
		super(MayaConverterCalcFunc, self).__init__()

		self.mcc_calculate_qpushbutton.clicked.connect(self.mcc_metric_dropdown_combobox_func)

	# CAVEAT : Value box and dropdown to choose type of metric
	def mcc_metric_dropdown_combobox_func(self):
		"""metric list and calculation to get cm

		:return:
		"""
		if self.mcc_metric_dropdown_combobox.currentText() == "inch":
			# print "inch"
			value = float(self.mcc_value_box_qlineedit.text())
			print "cm:", self.inch_to_cm(value)
			self.mcc_result_qlineedit.setText(unicode(self.inch_to_cm(value)))
		elif self.mcc_metric_dropdown_combobox.currentText() == "foot":
			# print "foot"
			value = float(self.mcc_value_box_qlineedit.text())
			print "cm:", self.feet_to_cm(value)
			self.mcc_result_qlineedit.setText(unicode(self.feet_to_cm(value)))
		elif self.mcc_metric_dropdown_combobox.currentText() == "metre":
			# print "metre"
			value = float(self.mcc_value_box_qlineedit.text())
			print "cm:", self.metre_to_cm(value)
			self.mcc_result_qlineedit.setText(unicode(self.metre_to_cm(value)))

	@staticmethod
	def inch_to_cm(value):
		"""1 inch = 2.54cm

		:param value: provide a number in float(decimal)
		:return: x cm
		"""
		inch = value
		cm = inch * 2.54
		return cm

	@staticmethod
	def feet_to_cm(value):
		"""1 ft = 30.48cm

		:param value: provide a number in float(decimal)
		:return: x cm
		"""
		feet = value
		cm = feet * 30.48
		return cm

	@staticmethod
	def metre_to_cm(value):
		"""1 m = 100cm

		:param value: provide a number in float(decimal)
		:return: x cm
		"""
		m = value
		cm = m * 100.0
		return cm


if __name__ == "__main__":
	print "This is Main MayaConverterCalcFunc"
else:
	print "This is MayaConverterCalcFunc"
