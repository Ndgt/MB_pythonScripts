from pyfbsdk import*
chara =  FBApplication().CurrentCharacter

SkeletonNodeId_CharacterPropertyName = {
    FBSkeletonNodeId.kFBSkeletonReferenceIndex : "ReferenceLink",
    FBSkeletonNodeId.kFBSkeletonHipsIndex : "HipsLink", 
    FBSkeletonNodeId.kFBSkeletonLeftHipIndex : "LeftUpLegLink",
    FBSkeletonNodeId.kFBSkeletonLeftKneeIndex : "LeftLegLink",
    FBSkeletonNodeId.kFBSkeletonLeftAnkleIndex : "LeftFootLink",
    FBSkeletonNodeId.kFBSkeletonLeftFootIndex : "LeftToeBaseLink",
    FBSkeletonNodeId.kFBSkeletonRightHipIndex : "RightUpLegLink",
    FBSkeletonNodeId.kFBSkeletonRightKneeIndex : "RightLegLink",
    FBSkeletonNodeId.kFBSkeletonRightAnkleIndex : "RightFootLink",
    FBSkeletonNodeId.kFBSkeletonRightFootIndex : "RightToeBaseLink",
    FBSkeletonNodeId.kFBSkeletonWaistIndex : "SpineLink",
    FBSkeletonNodeId.kFBSkeletonChestIndex : "Spine1Link",
    FBSkeletonNodeId.kFBSkeletonLeftCollarIndex : "LeftShoulderLink",
    FBSkeletonNodeId.kFBSkeletonLeftShoulderIndex : "LeftArmLink",
    FBSkeletonNodeId.kFBSkeletonLeftElbowIndex : "LeftForeArmLink",
    FBSkeletonNodeId.kFBSkeletonLeftWristIndex : "LeftHandLink",
    FBSkeletonNodeId.kFBSkeletonRightCollarIndex : "RightShoulderLink",
    FBSkeletonNodeId.kFBSkeletonRightShoulderIndex : "RightArmLink",
    FBSkeletonNodeId.kFBSkeletonRightElbowIndex : "RightForeArmLink",
    FBSkeletonNodeId.kFBSkeletonRightWristIndex : "RightHandLink",
    FBSkeletonNodeId.kFBSkeletonNeckIndex : "NeckLink",
    FBSkeletonNodeId.kFBSkeletonHeadIndex : "HeadLink",
    FBSkeletonNodeId.kFBSkeletonLeftThumbAIndex : "LeftHandThumb1Link",
    FBSkeletonNodeId.kFBSkeletonLeftThumbBIndex : "LeftHandThumb2Link",
    FBSkeletonNodeId.kFBSkeletonLeftThumbCIndex : "LeftHandThumb3Link",
    FBSkeletonNodeId.kFBSkeletonLeftIndexAIndex : "LeftHandIndex1Link",
    FBSkeletonNodeId.kFBSkeletonLeftIndexBIndex : "LeftHandIndex2Link",
    FBSkeletonNodeId.kFBSkeletonLeftIndexCIndex : "LeftHandIndex3Link",
    FBSkeletonNodeId.kFBSkeletonLeftMiddleAIndex : "LeftHandMiddle1Link",
    FBSkeletonNodeId.kFBSkeletonLeftMiddleBIndex : "LeftHandMiddle2Link",
    FBSkeletonNodeId.kFBSkeletonLeftMiddleCIndex : "LeftHandMiddle3Link",
    FBSkeletonNodeId.kFBSkeletonLeftRingAIndex : "LeftHandRing1Link",
    FBSkeletonNodeId.kFBSkeletonLeftRingBIndex : "LeftHandRing2Link",
    FBSkeletonNodeId.kFBSkeletonLeftRingCIndex : "LeftHandRing3Link",
    FBSkeletonNodeId.kFBSkeletonLeftPinkyAIndex : "LeftHandPinky1Link",
    FBSkeletonNodeId.kFBSkeletonLeftPinkyBIndex : "LeftHandPinky2Link",
    FBSkeletonNodeId.kFBSkeletonLeftPinkyCIndex : "LeftHandPinky3Link",
    FBSkeletonNodeId.kFBSkeletonRightThumbAIndex : "RightHandThumb1Link",
    FBSkeletonNodeId.kFBSkeletonRightThumbBIndex : "RightHandThumb2Link",
    FBSkeletonNodeId.kFBSkeletonRightThumbCIndex : "RightHandThumb3Link",
    FBSkeletonNodeId.kFBSkeletonRightIndexAIndex : "RightHandIndex1Link",
    FBSkeletonNodeId.kFBSkeletonRightIndexBIndex : "RightHandIndex2Link",
    FBSkeletonNodeId.kFBSkeletonRightIndexCIndex : "RightHandIndex3Link",
    FBSkeletonNodeId.kFBSkeletonRightMiddleAIndex : "RightHandMiddle1Link",
    FBSkeletonNodeId.kFBSkeletonRightMiddleBIndex : "RightHandMiddle2Link",
    FBSkeletonNodeId.kFBSkeletonRightMiddleCIndex : "RightHandMiddle3Link",
    FBSkeletonNodeId.kFBSkeletonRightRingAIndex : "RightHandRing1Link",
    FBSkeletonNodeId.kFBSkeletonRightRingBIndex : "RightHandRing2Link",
    FBSkeletonNodeId.kFBSkeletonRightRingCIndex : "RightHandRing3Link",
    FBSkeletonNodeId.kFBSkeletonRightPinkyAIndex : "RightHandPinky1Link",
    FBSkeletonNodeId.kFBSkeletonRightPinkyBIndex : "RightHandPinky2Link",
    FBSkeletonNodeId.kFBSkeletonRightPinkyCIndex : "RightHandPinky3Link",
}



def BoneNum(chara):
    returnNum = 0
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            returnNum += 1
    return returnNum

