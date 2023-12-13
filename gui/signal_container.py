from PySide6.QtCore import QObject, Signal

from gui.image import Image


# Video image input and analysis by openpose
class SignalContainer(QObject):
    update_image = Signal(Image)

class YOLOContainer(QObject):
    update_image = Signal(Image)

class PoseContainer(QObject):
    update_image = Signal(Image)


class DeepContainer(QObject):
    update_image = Signal(Image)


class FrequenceContainer(QObject):
    update_image = Signal(Image)


class DeepContainer(QObject):
    update_image = Signal(Image)

# result data for angle
class LabelContainer(QObject):
    update_label = Signal(str)


class LabelDeepContainer(QObject):
    update_label = Signal(str)

'''show Frequency between press'''
class FrequencyLabelContainer(QObject):
    update_label = Signal(str)

class PostureLabelContainer(QObject):
    update_label = Signal(str)
class DepthPostureLabelContainer(QObject):
    update_label = Signal(str)
class PositionLabelContainer(QObject):
    update_label = Signal(str)

class RateLabelContainer(QObject):
    update_label = Signal(str)

class DeepLabelResultContainer(QObject):
    update_label = Signal(str)

class FrequencyLabelResultContainer(QObject):
    update_label = Signal(str)

class PostureLabelResultContainer(QObject):
    update_label = Signal(str)

class textEditResultContainer(QObject):
    update_label = Signal(str)
class downloadButtonContainer(QObject):
    update_label = Signal(str)



