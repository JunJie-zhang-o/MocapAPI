




from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Pose:
    x:float
    y:float
    z:float
    rx:float
    ry:float
    rz:float


from dataclasses import dataclass


@dataclass
class Hips(Pose):
    """
    臀部
    """
    pass

@dataclass
class RightUpLeg(Pose):
    """
    右大腿
    """
    pass

@dataclass
class RightLeg(Pose):
    """
    右小腿
    """
    pass

@dataclass
class RightFoot(Pose):
    """
    右脚
    """
    pass

@dataclass
class LeftUpLeg(Pose):
    """
    左大腿
    """
    pass

@dataclass
class LeftLeg(Pose):
    """
    左小腿
    """
    pass

@dataclass
class LeftFoot(Pose):
    """
    左脚
    """
    pass

@dataclass
class Spine(Pose):
    """
    脊柱下部分
    """
    pass

@dataclass
class Spine1(Pose):
    """
    脊柱中部分
    """
    pass

@dataclass
class Spine2(Pose):
    """
    脊柱上部分
    """
    pass

@dataclass
class Neck(Pose):
    """
    颈部下部分
    """
    pass

@dataclass
class Neck1(Pose):
    """
    颈部上部分
    """
    pass

@dataclass
class Head(Pose):
    """
    头部
    """
    pass

@dataclass
class RightShoulder(Pose):
    """
    右肩
    """
    pass

@dataclass
class RightArm(Pose):
    """
    右大臂
    """
    pass

@dataclass
class RightForeArm(Pose):
    """
    右前臂
    """
    pass

@dataclass
class RightHand(Pose):
    """
    右手
    """
    pass

@dataclass
class RightHandThumb1(Pose):
    """
    右拇指指根
    """
    pass

@dataclass
class RightHandThumb2(Pose):
    """
    右拇指指中
    """
    pass

@dataclass
class RightHandThumb3(Pose):
    """
    右拇指指尖
    """
    pass

@dataclass
class RightInHandIndex(Pose):
    """
    右食指掌骨
    """
    pass

@dataclass
class RightHandIndex1(Pose):
    """
    右食指指根
    """
    pass

@dataclass
class RightHandIndex2(Pose):
    """
    右食指指中
    """
    pass

@dataclass
class RightHandIndex3(Pose):
    """
    右食指指尖
    """
    pass

@dataclass
class RightInHandMiddle(Pose):
    """
    右中指掌骨
    """
    pass

@dataclass
class RightHandMiddle1(Pose):
    """
    右中指指根
    """
    pass

@dataclass
class RightHandMiddle2(Pose):
    """
    右中指指中
    """
    pass

@dataclass
class RightHandMiddle3(Pose):
    """
    右中指指尖
    """
    pass

@dataclass
class RightInHandRing(Pose):
    """
    右无名指掌骨
    """
    pass

@dataclass
class RightHandRing1(Pose):
    """
    右无名指指根
    """
    pass

@dataclass
class RightHandRing2(Pose):
    """
    右无名指指中
    """
    pass

@dataclass
class RightHandRing3(Pose):
    """
    右无名指指尖
    """
    pass

@dataclass
class RightInHandPinky(Pose):
    """
    右小指掌骨
    """
    pass

@dataclass
class RightHandPinky1(Pose):
    """
    右小指指根
    """
    pass

@dataclass
class RightHandPinky2(Pose):
    """
    右小指指中
    """
    pass

@dataclass
class RightHandPinky3(Pose):
    """
    右小指指尖
    """
    pass

@dataclass
class LeftShoulder(Pose):
    """
    左肩
    """
    pass

@dataclass
class LeftArm(Pose):
    """
    左大臂
    """
    pass

@dataclass
class LeftForeArm(Pose):
    """
    左前臂
    """
    pass

@dataclass
class LeftHand(Pose):
    """
    左手
    """
    pass

@dataclass
class LeftHandThumb1(Pose):
    """
    左拇指指根
    """
    pass

@dataclass
class LeftHandThumb2(Pose):
    """
    左拇指指中
    """
    pass

@dataclass
class LeftHandThumb3(Pose):
    """
    左拇指指尖
    """
    pass

@dataclass
class LeftInHandIndex(Pose):
    """
    左食指掌骨
    """
    pass

@dataclass
class LeftHandIndex1(Pose):
    """
    左食指指根
    """
    pass

@dataclass
class LeftHandIndex2(Pose):
    """
    左食指指中
    """
    pass

@dataclass
class LeftHandIndex3(Pose):
    """
    左食指指尖
    """
    pass

@dataclass
class LeftInHandMiddle(Pose):
    """
    左中指掌骨
    """
    pass

@dataclass
class LeftHandMiddle1(Pose):
    """
    左中指指根
    """
    pass

@dataclass
class LeftHandMiddle2(Pose):
    """
    左中指指中
    """
    pass

@dataclass
class LeftHandMiddle3(Pose):
    """
    左中指指尖
    """
    pass

@dataclass
class LeftInHandRing(Pose):
    """
    左无名指掌骨
    """
    pass

@dataclass
class LeftHandRing1(Pose):
    """
    左无名指指根
    """
    pass

@dataclass
class LeftHandRing2(Pose):
    """
    左无名指指中
    """
    pass

@dataclass
class LeftHandRing3(Pose):
    """
    左无名指指尖
    """
    pass

@dataclass
class LeftInHandPinky(Pose):
    """
    左小指掌骨
    """
    pass

@dataclass
class LeftHandPinky1(Pose):
    """
    左小指指根
    """
    pass

@dataclass
class LeftHandPinky2(Pose):
    """
    左小指指中
    """
    pass

@dataclass
class LeftHandPinky3(Pose):
    """
    左小指指尖
    """
    pass






@dataclass
class MocapData:
    VALID_DATA_FMT:ClassVar[str] = "24s"*59
    FMT:ClassVar[str] = f"<2s4s2sss4s32s4s4s4s4s2s{VALID_DATA_FMT}"
    startFlag:str
    version:str
    datacount:str
    withDisp:str
    withReference:str
    avatarIndex:str
    avatarName:str
    frameIndex:str
    rotation:str
    timecode:str
    timecodeSubframe:str
    frameFlag:str
    hips: Hips
    rightUpLeg: RightUpLeg
    rightLeg: RightLeg
    rightFoot: RightFoot
    leftUpLeg: LeftUpLeg
    leftLeg: LeftLeg
    leftFoot: LeftFoot
    spine: Spine
    spine1: Spine1
    spine2: Spine2
    neck: Neck
    neck1: Neck1
    head: Head
    rightShoulder: RightShoulder
    rightArm: RightArm
    rightForeArm: RightForeArm
    rightHand: RightHand
    rightHandThumb1: RightHandThumb1
    rightHandThumb2: RightHandThumb2
    rightHandThumb3: RightHandThumb3
    rightInHandIndex: RightInHandIndex
    rightHandIndex1: RightHandIndex1
    rightHandIndex2: RightHandIndex2
    rightHandIndex3: RightHandIndex3
    rightInHandMiddle: RightInHandMiddle
    rightHandMiddle1: RightHandMiddle1
    rightHandMiddle2: RightHandMiddle2
    rightHandMiddle3: RightHandMiddle3
    rightInHandRing: RightInHandRing
    rightHandRing1: RightHandRing1
    rightHandRing2: RightHandRing2
    rightHandRing3: RightHandRing3
    rightInHandPinky: RightInHandPinky
    rightHandPinky1: RightHandPinky1
    rightHandPinky2: RightHandPinky2
    rightHandPinky3: RightHandPinky3
    leftShoulder: LeftShoulder
    leftArm: LeftArm
    leftForeArm: LeftForeArm
    leftHand: LeftHand
    leftHandThumb1: LeftHandThumb1
    leftHandThumb2: LeftHandThumb2
    leftHandThumb3: LeftHandThumb3
    leftInHandIndex: LeftInHandIndex
    leftHandIndex1: LeftHandIndex1
    leftHandIndex2: LeftHandIndex2
    leftHandIndex3: LeftHandIndex3
    leftInHandMiddle: LeftInHandMiddle
    leftHandMiddle1: LeftHandMiddle1
    leftHandMiddle2: LeftHandMiddle2
    leftHandMiddle3: LeftHandMiddle3
    leftInHandRing: LeftInHandRing
    leftHandRing1: LeftHandRing1
    leftHandRing2: LeftHandRing2
    leftHandRing3: LeftHandRing3
    leftInHandPinky: LeftInHandPinky
    leftHandPinky1:LeftHandPinky1
    leftHandPinky2:LeftHandPinky2
    leftHandPinky3:LeftHandPinky2

    @classmethod
    def getDefaultStartFlag(cls):
        return "ffdd"

    @classmethod
    def getDefaultFrameFlag(cls):
        return "ffee"
