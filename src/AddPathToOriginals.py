# -*- coding: utf-8 -*-

import sys,os,inspect
from pyfbsdk import *

system = FBSystem()
systemUIIdle = system.OnUIIdle

systemUIIdle.RemoveAll()

check = -1
def AddPathToOriginals(arg1:FBSystem, arg2:FBEvent):
    # �ēxAddPathToOriginals�֐������s���ꂽ���̂��߂�check�̒l�ŕ���
    global check
    if check == -1:
        check = 0

        # ���݂̃p�X���擾�i�z�z�v���O�C�����_�E�����[�h���Ă��炤�w���j
        CurrentFilePath = inspect.currentframe().f_code.co_filename
        CurrentDir = os.path.dirname(CurrentFilePath)

        # �w���t�H���_���ɂ����Ă���Apath��ǉ��������t�H���_�ւƃ��W���[�������p�X��ʂ�  
        # �����ł�OriginalSctipts�Ƃ��Ă��܂�
        targetPath = os.path.join(CurrentDir,"OriginalScripts")
        sys.path.append(targetPath)

    else:
        systemUIIdle.Remove(AddPathToOriginals)

systemUIIdle.Add(AddPathToOriginals)