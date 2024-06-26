#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mart 22, 2022, at 15:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from numpy import subtract
import telegram_send

import random
import telegram_send

import telegram_send

import telegram_send

from numpy import subtract


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'deney-negatif'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "expinfo"
expinfoClock = core.Clock()
colorblue = visual.ImageStim(
    win=win,
    name='colorblue', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
clickend1 = event.Mouse(win=win)
x, y = [None, None]
clickend1.mouseClock = core.Clock()
tamambuton = visual.ImageStim(
    win=win,
    name='tamambuton', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -450), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text = visual.TextStim(win=win, name='text',
    text='Sayın Katılımcı, \n\nÇalışmaya başlamadan önce tamamlamanız gereken bir adet form bulunmaktadır. Bu sayfanın en altında yer alan "TAMAM" butonuna tıkladığınızda önünüze Bilgilendirilmiş Onam Formu çıkacaktır. Bu formu dikkatlice okuyunuz. Bilgilendirmiş Onam Formu ile ilgili sorularınızı araştırmacıya sorabilirsiniz. Bilgilendirilmiş Onam Formunu okuduktan sonra devam etmek için ‘‘OKUDUM, ANLADIM, ONAYLIYORUM’’ butonuna tıklayınız.\n\n\nKatılımınız için teşekkür ederiz.\n',
    font='Open Sans',
    units='cm', pos=(0, 2), height=1.0, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "onam"
onamClock = core.Clock()
colorblue_2 = visual.ImageStim(
    win=win,
    name='colorblue_2', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
onaybuton = visual.ImageStim(
    win=win,
    name='onaybuton', 
    image='onay.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
clickend2 = event.Mouse(win=win)
x, y = [None, None]
clickend2.mouseClock = core.Clock()
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.25),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
adısoyadı = visual.TextStim(win=win, name='adısoyadı',
    text='Ad-Soyad',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
onamtext = visual.TextStim(win=win, name='onamtext',
    text='Sayın Katılımcı, \n\nBu çalışma İstanbul Sabahattin Zaim Üniversitesi İnsan ve Toplum Bilimleri Fakültesi Psikoloji Bölümü Dr. Öğr. Üyesi Yusuf BİLGE danışmanlığında, İstanbul Sabahattin Zaim Üniversitesi Lisansüstü Eğitim Enstitüsü Klinik Psikoloji yüksek lisans öğrencisi Kübra MAHMUT ÖNALAN tarafından yüksek lisans tezi ve Bilimsel Araştırma Projesi (BAP) kapsamında yürütülmektedir.\n\nKatılacağınız çalışma beş aşamadan oluşan bir psikoloji çalışmasıdır. Her aşama ayrı ayrı bölümlendirilmiş olup, her aşamanın başında geçtiğiniz aşamaya göre bir bilgilendirme ekranı ile karşılaşacaksınız. Geçtiğiniz aşama ile ilgili yönergeler araştırmacının kendisi tarafından verilecektir. Tüm aşamalar yaklaşık 30 dakika sürecektir. \n\nBu çalışmaya katılmak tamamen gönüllülük esasına dayanmaktadır. Bu formu okuyup onaylamanız, araştırmaya katılmayı kabul ettiğiniz anlamına gelecektir. Ancak, çalışmaya katılmama veya katıldıktan sonra herhangi bir anda çalışmayı bırakma hakkına da sahipsiniz. Bu çalışmadan elde edilecek bilgiler tamamen araştırma amacı ile kullanılacak olup kişisel bilgileriniz gizli tutulacaktır. Araştırmada kişisel veri toplanacağından 6698 sayılı kişisel verilerin korunması kanunu ve ilgili mevzuat uyarınca kişisel verileri korumak amacıyla gerekli tüm tedbirler alınacaktır. \n\nÇalışmanın sonunda araştırmacı çalışmanın içeriğiyle ilgili kısa bir görüşme gerçekleştirecektir. Görüşmeden sonra araştırmacı çalışma ile ilgili sorularınız için iletişim bilgilerini paylaşarak çalışmayı sonlandıracaktır.\n',
    font='Open Sans',
    units='cm', pos=(0, 3), height=0.7, wrapWidth=50.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "birinciasamainfo"
birinciasamainfoClock = core.Clock()
colorblue_3 = visual.ImageStim(
    win=win,
    name='colorblue_3', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
tamambuton_2 = visual.ImageStim(
    win=win,
    name='tamambuton_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
olcekasaması1 = visual.TextStim(win=win, name='olcekasaması1',
    text='Bilgilendirilmiş Onam Formunu onayladınız. Çalışmanın ilk aşaması olan "Ölçek Aşaması"na geçtiniz. Araştırmacı size bu aşama ile ilgili gerekli açıklamaları yapacaktır.\n\nGerekli açıklamalar yapıldıktan sonra "TAMAM" butonuna basarak ölçek aşamasına geçebilirsiniz. Açıklama yapılmadan önce "TAMAM" butonuna basmayınız. ',
    font='Open Sans',
    units='cm', pos=(0, 0), height=0.9, wrapWidth=35.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "duygular"
duygularClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=None, ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
ratingText = visual.TextStim(win=win, name='ratingText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slidersoru = visual.TextStim(win=win, name='slidersoru',
    text='Aşağıdaki duyguyu ŞU ANDA ne düzeyde hissettiğinizi çizgiyi sürükleyerek puanlayınız.',
    font='Open Sans',
    pos=[0,0], height=0.04, wrapWidth=50.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
trialbitiren = event.Mouse(win=win)
x, y = [None, None]
trialbitiren.mouseClock = core.Clock()
bitti = visual.ImageStim(
    win=win,
    name='bitti', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
negatiftext = visual.TextStim(win=win, name='negatiftext',
    text='',
    font='Open Sans',
    pos=(-0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
pozitiftext = visual.TextStim(win=win, name='pozitiftext',
    text='',
    font='Open Sans',
    pos=(0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
notrtext = visual.TextStim(win=win, name='notrtext',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 2.4), height=3.0, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
fakemarker_2 = visual.Rect(
    win=win, name='fakemarker_2',
    width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
    ori=0.0, pos=(-0.5, -0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=1.0, depth=-9.0, interpolate=True)
arrows = visual.TextStim(win=win, name='arrows',
    text='← →',
    font='Open Sans',
    pos=(-0.5, -0.02), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "duygular"
duygularClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=None, ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
ratingText = visual.TextStim(win=win, name='ratingText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slidersoru = visual.TextStim(win=win, name='slidersoru',
    text='Aşağıdaki duyguyu ŞU ANDA ne düzeyde hissettiğinizi çizgiyi sürükleyerek puanlayınız.',
    font='Open Sans',
    pos=[0,0], height=0.04, wrapWidth=50.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
trialbitiren = event.Mouse(win=win)
x, y = [None, None]
trialbitiren.mouseClock = core.Clock()
bitti = visual.ImageStim(
    win=win,
    name='bitti', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
negatiftext = visual.TextStim(win=win, name='negatiftext',
    text='',
    font='Open Sans',
    pos=(-0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
pozitiftext = visual.TextStim(win=win, name='pozitiftext',
    text='',
    font='Open Sans',
    pos=(0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
notrtext = visual.TextStim(win=win, name='notrtext',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 2.4), height=3.0, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
fakemarker_2 = visual.Rect(
    win=win, name='fakemarker_2',
    width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
    ori=0.0, pos=(-0.5, -0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=1.0, depth=-9.0, interpolate=True)
arrows = visual.TextStim(win=win, name='arrows',
    text='← →',
    font='Open Sans',
    pos=(-0.5, -0.02), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "subtracct"
subtracctClock = core.Clock()

# Initialize components for Routine "ruminasyon"
ruminasyonClock = core.Clock()
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=None, ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=0, readOnly=False)
ruminasyonsorular = visual.TextStim(win=win, name='ruminasyonsorular',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 4), height=1.5, wrapWidth=35.0, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
bitti_2 = visual.ImageStim(
    win=win,
    name='bitti_2', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
trialbitiren_2 = event.Mouse(win=win)
x, y = [None, None]
trialbitiren_2.mouseClock = core.Clock()
ratingText_2 = visual.TextStim(win=win, name='ratingText_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ruminasyonklvz = visual.TextStim(win=win, name='ruminasyonklvz',
    text='Aşağıdaki maddeyi, ŞU ANDA nasıl hissettiğinizi ya da düşündüğünüzü göz önünde bulundurarak çizgiyi sürükleyerek puanlayınız.',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
fakemarker_3 = visual.Rect(
    win=win, name='fakemarker_3',
    width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
    ori=0.0, pos=(-0.5, -0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=1.0, depth=-7.0, interpolate=True)
negatiftext_2 = visual.TextStim(win=win, name='negatiftext_2',
    text='Hiç Doğru Değil',
    font='Open Sans',
    pos=(-0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
pozitiftext_2 = visual.TextStim(win=win, name='pozitiftext_2',
    text='Tümüyle Doğru',
    font='Open Sans',
    pos=(0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
arrows_2 = visual.TextStim(win=win, name='arrows_2',
    text='← →',
    font='Open Sans',
    pos=(-0.5, -0.02), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "session_end"
session_endClock = core.Clock()

# Initialize components for Routine "navonbilgi"
navonbilgiClock = core.Clock()
colorblue_4 = visual.ImageStim(
    win=win,
    name='colorblue_4', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
tamam4 = visual.ImageStim(
    win=win,
    name='tamam4', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
orneknavonimg = visual.ImageStim(
    win=win,
    name='orneknavonimg', units='cm', 
    image='orneknavon.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Ölçek aşamasını tamamladınız. Çalışmanın ikinci aşaması olan "Dikkat Testi Aşaması"na geçtiniz. Lütfen araştırmacıyı bekleyiniz. Araştırmacı size bu aşama ile ilgili gerekli açıklamaları yapacaktır.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAraştırmacı size gerekli açıklamaları sunduktan sonra "TAMAM" butonuna tıklayabilirsiniz. Açıklama yapılmadan önce "TAMAM" butonuna basmayınız. ',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
colorblue_8 = visual.ImageStim(
    win=win,
    name='colorblue_8', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test başlıyor! Elinizin konumunu klavyede belirlenen harflere göre ayarlayın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "navon_pilot"
navon_pilotClock = core.Clock()
letter_2 = visual.ImageStim(
    win=win,
    name='letter_2', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(8,8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.4, wrapWidth=None, ori=0.0, 
    color=[-1.0, -1.0, -1.0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()
noise_4 = visual.NoiseStim(
    win=win, name='noise_4',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(8, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-4.0)
noise_4.buildNoise()

# Initialize components for Routine "dogru_2"
dogru_2Clock = core.Clock()
dogrusu = visual.TextStim(win=win, name='dogrusu',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
texttt = visual.TextStim(win=win, name='texttt',
    text='Doğru Cevap:',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "pilot_navon"
pilot_navonClock = core.Clock()
colorblue_7 = visual.ImageStim(
    win=win,
    name='colorblue_7', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
pilotnavontxt = visual.TextStim(win=win, name='pilotnavontxt',
    text='Deneme aşaması sona ermiştir.\n\nBu aşamadan sonraki performansınız değerlendirilecektir.\n\nDeneme aşamasını tekrar etmek için "Tekrar" butonuna, test aşamasına geçmek için hazır olduğunuzda "Tamam" butonuna basın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
tamam4_2 = visual.ImageStim(
    win=win,
    name='tamam4_2', units='cm', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(6,-6), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
tekrarbuttonimg = visual.ImageStim(
    win=win,
    name='tekrarbuttonimg', units='cm', 
    image='bos.png', mask=None,
    ori=0.0, pos=(-6, -6), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
tekrarbutton = visual.ButtonStim(win, 
    text='Tekrar?', font='Open Sans',
    pos=(-6, -6),units='cm',
    letterHeight=1.0,
    size=(6, 1.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='tekrarbutton'
)
tekrarbutton.buttonClock = core.Clock()
tamambutton = visual.ButtonStim(win, 
    text=None, font='Open Sans',
    pos=(6,-6),units='cm',
    letterHeight=1.0,
    size=(6, 1.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='tamambutton'
)
tamambutton.buttonClock = core.Clock()
tekrartexttt = visual.TextStim(win=win, name='tekrartexttt',
    text='TEKRAR',
    font='Open Sans',
    units='cm', pos=(-6,-6), height=1.0, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.4431, 0.0275], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
colorblue_8 = visual.ImageStim(
    win=win,
    name='colorblue_8', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test başlıyor! Elinizin konumunu klavyede belirlenen harflere göre ayarlayın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "navon_1"
navon_1Clock = core.Clock()
letter = visual.ImageStim(
    win=win,
    name='letter', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(8,8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.4, wrapWidth=None, ori=0.0, 
    color=[-1.0, -1.0, -1.0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
noise = visual.NoiseStim(
    win=win, name='noise',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(8, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
noise.buildNoise()

# Initialize components for Routine "interval"
intervalClock = core.Clock()
countdown = visual.TextStim(win=win, name='countdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
timer_line = visual.Rect(
    win=win, name='timer_line',units='cm', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, -5),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=None, depth=-2.0, interpolate=True)
mola = visual.TextStim(win=win, name='mola',
    text='-Mola-',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
colorblue_8 = visual.ImageStim(
    win=win,
    name='colorblue_8', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test başlıyor! Elinizin konumunu klavyede belirlenen harflere göre ayarlayın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "navon_2"
navon_2Clock = core.Clock()
letter_3 = visual.ImageStim(
    win=win,
    name='letter_3', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(8,8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fix_3 = visual.TextStim(win=win, name='fix_3',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.4, wrapWidth=None, ori=0.0, 
    color=[-1.0, -1.0, -1.0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()
noise_5 = visual.NoiseStim(
    win=win, name='noise_5',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(8, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
noise_5.buildNoise()

# Initialize components for Routine "session_end"
session_endClock = core.Clock()

# Initialize components for Routine "cattellbilgi"
cattellbilgiClock = core.Clock()
colorblue_5 = visual.ImageStim(
    win=win,
    name='colorblue_5', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
tamam5 = visual.ImageStim(
    win=win,
    name='tamam5', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cattelllbilgitxt1 = visual.TextStim(win=win, name='cattelllbilgitxt1',
    text='Dikkat Testi Aşamasını tamamladınız. Çalışmanın üçüncü aşaması olan "Zeka Testi Aşaması"na geçtiniz. Lütfen araştırmacıyı bekleyiniz. Araştırmacı size bu aşama ile ilgili gerekli açıklamaları yapacaktır.\n\nAraştırmacı size gerekli açıklamaları sunduktan sonra "TAMAM" butonuna tıklayabilirsiniz. Açıklama yapılmadan önce "TAMAM" butonuna basmayınız. ',
    font='Open Sans',
    units='cm', pos=(0, 0), height=0.9, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cattell6"
cattell6Clock = core.Clock()
ornek = visual.ImageStim(
    win=win,
    name='ornek', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
a = visual.ImageStim(
    win=win,
    name='a', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(-13.25,-6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
b = visual.ImageStim(
    win=win,
    name='b', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(-7.95,-6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
c = visual.ImageStim(
    win=win,
    name='c', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(-2.65,-6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
d = visual.ImageStim(
    win=win,
    name='d', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(2.65, -6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
e = visual.ImageStim(
    win=win,
    name='e', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(7.95, -6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
f = visual.ImageStim(
    win=win,
    name='f', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(13.25, -6), size=[4,4],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
instructionn = visual.TextStim(win=win, name='instructionn',
    text='',
    font='Open Sans',
    units='cm', pos=[0,0], height=0.8, wrapWidth=30.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
süre = visual.TextStim(win=win, name='süre',
    text='',
    font='Open Sans',
    units='cm', pos=(23, -14), height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
noise_2 = visual.NoiseStim(
    win=win, name='noise_2',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(25, 12), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=64, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_2.buildNoise()
timeuptext = visual.TextStim(win=win, name='timeuptext',
    text='SÜRENİZ DOLDU.\nCEVABINIZI İŞARETLEYİN.',
    font='Impact',
    units='cm', pos=[0,0], height=2.0, wrapWidth=18.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
soundd = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='soundd')
soundd.setVolume(1.0)
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "cattell2_2"
cattell2_2Clock = core.Clock()
harfsoru = visual.TextStim(win=win, name='harfsoru',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=40.0, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
kılavuz = visual.TextStim(win=win, name='kılavuz',
    text='Aşağıdaki harflerin oluşturduğu örüntüde "?" yerine aşağıdakilerden hangisi gelmelidir?',
    font='Open Sans',
    units='cm', pos=(0, 5), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
butoncvp_1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=(-10, -8),units='cm',
    letterHeight=1.0,
    size=(3,2), borderWidth=0.0,
    fillColor=[-1.0000, -0.0588, 0.6863], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='butoncvp_1'
)
butoncvp_1.buttonClock = core.Clock()
butoncvp_2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=(-5, -8),units='cm',
    letterHeight=1.0,
    size=(3,2), borderWidth=0.0,
    fillColor=[-1.0000, -0.0588, 0.6863], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='butoncvp_2'
)
butoncvp_2.buttonClock = core.Clock()
butoncvp_3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=(0, -8),units='cm',
    letterHeight=1.0,
    size=(3,2), borderWidth=0.0,
    fillColor=[-1.0000, -0.0588, 0.6863], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='butoncvp_3'
)
butoncvp_3.buttonClock = core.Clock()
butoncvp_4 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=(5, -8),units='cm',
    letterHeight=1.0,
    size=(3,2), borderWidth=0.0,
    fillColor=[-1.0000, -0.0588, 0.6863], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='butoncvp_4'
)
butoncvp_4.buttonClock = core.Clock()
butoncvp_5 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=(10, -8),units='cm',
    letterHeight=1.0,
    size=(3,2), borderWidth=0.0,
    fillColor=[-1.0000, -0.0588, 0.6863], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='butoncvp_5'
)
butoncvp_5.buttonClock = core.Clock()
noise_3 = visual.NoiseStim(
    win=win, name='noise_3',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, -1), size=(40, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=64, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-7.0)
noise_3.buildNoise()
süre_2 = visual.TextStim(win=win, name='süre_2',
    text='',
    font='Open Sans',
    units='cm', pos=(23, -14), height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
timeuptext_2 = visual.TextStim(win=win, name='timeuptext_2',
    text='SÜRENİZ DOLDU.\nCEVABINIZI İŞARETLEYİN.',
    font='Impact',
    units='cm', pos=[0,0], height=2.0, wrapWidth=18.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
soundd = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='soundd')
soundd.setVolume(1.0)
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "toplampuan"
toplampuanClock = core.Clock()
toplam = visual.TextStim(win=win, name='toplam',
    text='ZEKA TESTİ SONUCU:\n\n2/10',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
tamam7_2 = visual.ImageStim(
    win=win,
    name='tamam7_2', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "session_end"
session_endClock = core.Clock()

# Initialize components for Routine "testbilgi"
testbilgiClock = core.Clock()
colorblue_9 = visual.ImageStim(
    win=win,
    name='colorblue_9', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
tamam7 = visual.ImageStim(
    win=win,
    name='tamam7', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sonasamabilgitxt = visual.TextStim(win=win, name='sonasamabilgitxt',
    text='Zeka Testi Aşamasını tamamladınız. Çalışmanın dördüncü aşaması olan "Ölçek Aşaması"na geçtiniz. Lütfen araştırmacıyı bekleyiniz. Araştırmacı size bu aşama ile ilgili gerekli açıklamaları yapacaktır.\n\nAraştırmacı size gerekli açıklamaları sunduktan sonra "TAMAM" butonuna tıklayabilirsiniz. Açıklama yapılmadan önce "TAMAM" butonuna basmayınız. ',
    font='Open Sans',
    units='cm', pos=(0, 0), height=0.9, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "duygular"
duygularClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=None, ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
ratingText = visual.TextStim(win=win, name='ratingText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slidersoru = visual.TextStim(win=win, name='slidersoru',
    text='Aşağıdaki duyguyu ŞU ANDA ne düzeyde hissettiğinizi çizgiyi sürükleyerek puanlayınız.',
    font='Open Sans',
    pos=[0,0], height=0.04, wrapWidth=50.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
trialbitiren = event.Mouse(win=win)
x, y = [None, None]
trialbitiren.mouseClock = core.Clock()
bitti = visual.ImageStim(
    win=win,
    name='bitti', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
negatiftext = visual.TextStim(win=win, name='negatiftext',
    text='',
    font='Open Sans',
    pos=(-0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
pozitiftext = visual.TextStim(win=win, name='pozitiftext',
    text='',
    font='Open Sans',
    pos=(0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
notrtext = visual.TextStim(win=win, name='notrtext',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 2.4), height=3.0, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
fakemarker_2 = visual.Rect(
    win=win, name='fakemarker_2',
    width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
    ori=0.0, pos=(-0.5, -0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=1.0, depth=-9.0, interpolate=True)
arrows = visual.TextStim(win=win, name='arrows',
    text='← →',
    font='Open Sans',
    pos=(-0.5, -0.02), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "hataruminasyon"
hataruminasyonClock = core.Clock()
hataslider = visual.Slider(win=win, name='hataslider',
    startValue=None, size=(1, 0.05), pos=(0, -0.1), units=None,
    labels=("Hiçbir Zaman", "Biraz", "Orta Düzeyde", "Çok Fazla"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor=[-1.0000, -0.0588, 0.6863], borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=0, readOnly=False)
sorular_2 = visual.TextStim(win=win, name='sorular_2',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 4), height=1.5, wrapWidth=40.0, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
tamam8 = visual.ImageStim(
    win=win,
    name='tamam8', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
hatarumklvztxt = visual.TextStim(win=win, name='hatarumklvztxt',
    text='Aşağıdaki verilen ifadeyi katıldığınız BU ÇALIŞMA İLE İLGİLİ deneyiminizi göz önünde bulundurarak puanlayınız.',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ruminasyon"
ruminasyonClock = core.Clock()
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=None, ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=0, readOnly=False)
ruminasyonsorular = visual.TextStim(win=win, name='ruminasyonsorular',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 4), height=1.5, wrapWidth=35.0, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
bitti_2 = visual.ImageStim(
    win=win,
    name='bitti_2', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
trialbitiren_2 = event.Mouse(win=win)
x, y = [None, None]
trialbitiren_2.mouseClock = core.Clock()
ratingText_2 = visual.TextStim(win=win, name='ratingText_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ruminasyonklvz = visual.TextStim(win=win, name='ruminasyonklvz',
    text='Aşağıdaki maddeyi, ŞU ANDA nasıl hissettiğinizi ya da düşündüğünüzü göz önünde bulundurarak çizgiyi sürükleyerek puanlayınız.',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
fakemarker_3 = visual.Rect(
    win=win, name='fakemarker_3',
    width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
    ori=0.0, pos=(-0.5, -0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=1.0, depth=-7.0, interpolate=True)
negatiftext_2 = visual.TextStim(win=win, name='negatiftext_2',
    text='Hiç Doğru Değil',
    font='Open Sans',
    pos=(-0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
pozitiftext_2 = visual.TextStim(win=win, name='pozitiftext_2',
    text='Tümüyle Doğru',
    font='Open Sans',
    pos=(0.5, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
arrows_2 = visual.TextStim(win=win, name='arrows_2',
    text='← →',
    font='Open Sans',
    pos=(-0.5, -0.02), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.0588, 0.6863], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "navonbilgi2"
navonbilgi2Clock = core.Clock()
colorblue_10 = visual.ImageStim(
    win=win,
    name='colorblue_10', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
tamam6 = visual.ImageStim(
    win=win,
    name='tamam6', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.42), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Ölçek Aşamasını tamamladınız. Çalışmanın son aşaması olan "Dikkat Testi Aşaması"na geçtiniz. Lütfen araştırmacıyı bekleyiniz. Araştırmacı size bu aşama ile ilgili gerekli açıklamaları yapacaktır.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAraştırmacı size gerekli açıklamaları sunduktan sonra "TAMAM" butonuna tıklayabilirsiniz. Açıklama yapılmadan önce "TAMAM" butonuna basmayınız. ',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
orneknavonimg_2 = visual.ImageStim(
    win=win,
    name='orneknavonimg_2', units='cm', 
    image='orneknavon.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
colorblue_8 = visual.ImageStim(
    win=win,
    name='colorblue_8', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test başlıyor! Elinizin konumunu klavyede belirlenen harflere göre ayarlayın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "navon_3"
navon_3Clock = core.Clock()
letter_4 = visual.ImageStim(
    win=win,
    name='letter_4', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(8,8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fix_4 = visual.TextStim(win=win, name='fix_4',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.4, wrapWidth=None, ori=0.0, 
    color=[-1.0, -1.0, -1.0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()
noise_6 = visual.NoiseStim(
    win=win, name='noise_6',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(8, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
noise_6.buildNoise()

# Initialize components for Routine "interval"
intervalClock = core.Clock()
countdown = visual.TextStim(win=win, name='countdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
timer_line = visual.Rect(
    win=win, name='timer_line',units='cm', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, -5),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
    opacity=None, depth=-2.0, interpolate=True)
mola = visual.TextStim(win=win, name='mola',
    text='-Mola-',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
colorblue_8 = visual.ImageStim(
    win=win,
    name='colorblue_8', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Test başlıyor! Elinizin konumunu klavyede belirlenen harflere göre ayarlayın.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "navon_4"
navon_4Clock = core.Clock()
letter_5 = visual.ImageStim(
    win=win,
    name='letter_5', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(8,8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fix_5 = visual.TextStim(win=win, name='fix_5',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.4, wrapWidth=None, ori=0.0, 
    color=[-1.0, -1.0, -1.0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()
noise_7 = visual.NoiseStim(
    win=win, name='noise_7',units='cm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(8, 8), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
noise_7.buildNoise()

# Initialize components for Routine "session_end"
session_endClock = core.Clock()

# Initialize components for Routine "expfin"
expfinClock = core.Clock()
colorblue_11 = visual.ImageStim(
    win=win,
    name='colorblue_11', 
    image='mavi.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
tamamm = visual.ImageStim(
    win=win,
    name='tamamm', 
    image='tamam.png', mask=None,
    ori=0.0, pos=(0, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
finishingtxt = visual.TextStim(win=win, name='finishingtxt',
    text='Çalışmanın tüm aşamalarını tamamladınız. Çalışmaya katılımınız için teşekkür ederiz.  \n\nAraştırmacı çalışma hakkında bilgilendirme yapmak için kısa bir görüşme gerçekleştirecektir. Lütfen şimdi "TAMAM" butonuna basarak deneyi sonlandırınız.',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=45.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "finnishhhhhh"
finnishhhhhhClock = core.Clock()
key_resp_4 = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "expinfo"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the clickend1
clickend1.clicked_name = []
gotValidClick = False  # until a click is received
tamambuton.setImage('tamam.png')
# keep track of which components have finished
expinfoComponents = [colorblue, clickend1, tamambuton, text]
for thisComponent in expinfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
expinfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "expinfo"-------
while continueRoutine:
    # get current time
    t = expinfoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=expinfoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue* updates
    if colorblue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue.frameNStart = frameN  # exact frame index
        colorblue.tStart = t  # local t and not account for scr refresh
        colorblue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue, 'tStartRefresh')  # time at next scr refresh
        colorblue.setAutoDraw(True)
    # *clickend1* updates
    if clickend1.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        clickend1.frameNStart = frameN  # exact frame index
        clickend1.tStart = t  # local t and not account for scr refresh
        clickend1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(clickend1, 'tStartRefresh')  # time at next scr refresh
        clickend1.status = STARTED
        clickend1.mouseClock.reset()
        prevButtonState = clickend1.getPressed()  # if button is down already this ISN'T a new click
    if clickend1.status == STARTED:  # only update if started and not finished!
        buttons = clickend1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamambuton)
                    clickableList = tamambuton
                except:
                    clickableList = [tamambuton]
                for obj in clickableList:
                    if obj.contains(clickend1):
                        gotValidClick = True
                        clickend1.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamambuton* updates
    if tamambuton.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamambuton.frameNStart = frameN  # exact frame index
        tamambuton.tStart = t  # local t and not account for scr refresh
        tamambuton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamambuton, 'tStartRefresh')  # time at next scr refresh
        tamambuton.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expinfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "expinfo"-------
for thisComponent in expinfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "expinfo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
isim = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='isim')
thisExp.addLoop(isim)  # add the loop to the experiment
thisIsim = isim.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIsim.rgb)
if thisIsim != None:
    for paramName in thisIsim:
        exec('{} = thisIsim[paramName]'.format(paramName))

for thisIsim in isim:
    currentLoop = isim
    # abbreviate parameter names if possible (e.g. rgb = thisIsim.rgb)
    if thisIsim != None:
        for paramName in thisIsim:
            exec('{} = thisIsim[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "onam"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the clickend2
    clickend2.clicked_name = []
    gotValidClick = False  # until a click is received
    textbox.reset()
    # keep track of which components have finished
    onamComponents = [colorblue_2, onaybuton, clickend2, textbox, adısoyadı, onamtext]
    for thisComponent in onamComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    onamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "onam"-------
    while continueRoutine:
        # get current time
        t = onamClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=onamClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colorblue_2* updates
        if colorblue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            colorblue_2.frameNStart = frameN  # exact frame index
            colorblue_2.tStart = t  # local t and not account for scr refresh
            colorblue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colorblue_2, 'tStartRefresh')  # time at next scr refresh
            colorblue_2.setAutoDraw(True)
        
        # *onaybuton* updates
        if onaybuton.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            onaybuton.frameNStart = frameN  # exact frame index
            onaybuton.tStart = t  # local t and not account for scr refresh
            onaybuton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(onaybuton, 'tStartRefresh')  # time at next scr refresh
            onaybuton.setAutoDraw(True)
        # *clickend2* updates
        if clickend2.status == NOT_STARTED and t >= 5-frameTolerance:
            # keep track of start time/frame for later
            clickend2.frameNStart = frameN  # exact frame index
            clickend2.tStart = t  # local t and not account for scr refresh
            clickend2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clickend2, 'tStartRefresh')  # time at next scr refresh
            clickend2.status = STARTED
            clickend2.mouseClock.reset()
            prevButtonState = clickend2.getPressed()  # if button is down already this ISN'T a new click
        if clickend2.status == STARTED:  # only update if started and not finished!
            buttons = clickend2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(onaybuton)
                        clickableList = onaybuton
                    except:
                        clickableList = [onaybuton]
                    for obj in clickableList:
                        if obj.contains(clickend2):
                            gotValidClick = True
                            clickend2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        
        # *adısoyadı* updates
        if adısoyadı.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            adısoyadı.frameNStart = frameN  # exact frame index
            adısoyadı.tStart = t  # local t and not account for scr refresh
            adısoyadı.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(adısoyadı, 'tStartRefresh')  # time at next scr refresh
            adısoyadı.setAutoDraw(True)
        
        # *onamtext* updates
        if onamtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            onamtext.frameNStart = frameN  # exact frame index
            onamtext.tStart = t  # local t and not account for scr refresh
            onamtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(onamtext, 'tStartRefresh')  # time at next scr refresh
            onamtext.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in onamComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "onam"-------
    for thisComponent in onamComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    isim.addData('onaybuton.started', onaybuton.tStartRefresh)
    isim.addData('onaybuton.stopped', onaybuton.tStopRefresh)
    # store data for isim (TrialHandler)
    isim.addData('textbox.text',textbox.text)
    isim.addData('textbox.started', textbox.tStartRefresh)
    isim.addData('textbox.stopped', textbox.tStopRefresh)
    isim.addData('adısoyadı.started', adısoyadı.tStartRefresh)
    isim.addData('adısoyadı.stopped', adısoyadı.tStopRefresh)
    # the Routine "onam" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'isim'

# get names of stimulus parameters
if isim.trialList in ([], [None], None):
    params = []
else:
    params = isim.trialList[0].keys()
# save data for this loop
isim.saveAsExcel(filename + '.xlsx', sheetName='isim',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
isim.saveAsText(filename + 'isim.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "birinciasamainfo"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
tamambuton_2.setImage('tamam.png')
# keep track of which components have finished
birinciasamainfoComponents = [colorblue_3, mouse_5, tamambuton_2, olcekasaması1]
for thisComponent in birinciasamainfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
birinciasamainfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "birinciasamainfo"-------
while continueRoutine:
    # get current time
    t = birinciasamainfoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=birinciasamainfoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_3* updates
    if colorblue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_3.frameNStart = frameN  # exact frame index
        colorblue_3.tStart = t  # local t and not account for scr refresh
        colorblue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_3, 'tStartRefresh')  # time at next scr refresh
        colorblue_3.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamambuton_2)
                    clickableList = tamambuton_2
                except:
                    clickableList = [tamambuton_2]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamambuton_2* updates
    if tamambuton_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamambuton_2.frameNStart = frameN  # exact frame index
        tamambuton_2.tStart = t  # local t and not account for scr refresh
        tamambuton_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamambuton_2, 'tStartRefresh')  # time at next scr refresh
        tamambuton_2.setAutoDraw(True)
    
    # *olcekasaması1* updates
    if olcekasaması1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        olcekasaması1.frameNStart = frameN  # exact frame index
        olcekasaması1.tStart = t  # local t and not account for scr refresh
        olcekasaması1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(olcekasaması1, 'tStartRefresh')  # time at next scr refresh
        olcekasaması1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in birinciasamainfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "birinciasamainfo"-------
for thisComponent in birinciasamainfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_5.getPos()
buttons = mouse_5.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamambuton_2)
        clickableList = tamambuton_2
    except:
        clickableList = [tamambuton_2]
    for obj in clickableList:
        if obj.contains(mouse_5):
            gotValidClick = True
            mouse_5.clicked_name.append(obj.name)
thisExp.addData('mouse_5.x', x)
thisExp.addData('mouse_5.y', y)
thisExp.addData('mouse_5.leftButton', buttons[0])
thisExp.addData('mouse_5.midButton', buttons[1])
thisExp.addData('mouse_5.rightButton', buttons[2])
if len(mouse_5.clicked_name):
    thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
thisExp.addData('olcekasaması1.started', olcekasaması1.tStartRefresh)
thisExp.addData('olcekasaması1.stopped', olcekasaması1.tStopRefresh)
# the Routine "birinciasamainfo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
duygu1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('duygusorular.xlsx', selection='0'),
    seed=None, name='duygu1')
thisExp.addLoop(duygu1)  # add the loop to the experiment
thisDuygu1 = duygu1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDuygu1.rgb)
if thisDuygu1 != None:
    for paramName in thisDuygu1:
        exec('{} = thisDuygu1[paramName]'.format(paramName))

for thisDuygu1 in duygu1:
    currentLoop = duygu1
    # abbreviate parameter names if possible (e.g. rgb = thisDuygu1.rgb)
    if thisDuygu1 != None:
        for paramName in thisDuygu1:
            exec('{} = thisDuygu1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "duygular"-------
    continueRoutine = True
    # update component parameters for each repeat
    #yanda olması için exp değerleri: (0.55, -.095)
    thisPos = 0
    marker = slider.getMarkerPos()
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
        labels=("0", "10","20", "30", "40", "50", "60", "70", "80", "90", "100"), ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=5.0,
        style='rating', styleTweaks=(), opacity=1,
        color='black', fillColor='black', borderColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, depth=-1, readOnly=False)
    slider.marker = visual.Rect(
        win=win, name='polygon',units=None, 
        width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
        ori=0.0, pos=(0,-3),
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
        opacity=None, depth=-9.0, interpolate=True)
    slider.tickLines.opacities = 0
    slider.reset()
    # setup some python lists for storing info about the trialbitiren
    trialbitiren.clicked_name = []
    gotValidClick = False  # until a click is received
    bitti.setImage('tamam.png')
    negatiftext.setText(negatif)
    pozitiftext.setText(pozitif)
    notrtext.setText(notr)
    # keep track of which components have finished
    duygularComponents = [slider, ratingText, slidersoru, trialbitiren, bitti, negatiftext, pozitiftext, notrtext, fakemarker_2, arrows]
    for thisComponent in duygularComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    duygularClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "duygular"-------
    while continueRoutine:
        # get current time
        t = duygularClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=duygularClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if slider.getMarkerPos() != None:
            thisPos = (slider.getMarkerPos() / 100)-0.5
            marker = int(slider.getMarkerPos())
        else:
            marker = ""
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *ratingText* updates
        if ratingText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ratingText.frameNStart = frameN  # exact frame index
            ratingText.tStart = t  # local t and not account for scr refresh
            ratingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText, 'tStartRefresh')  # time at next scr refresh
            ratingText.setAutoDraw(True)
        if ratingText.status == STARTED:  # only update if drawing
            ratingText.setPos((thisPos, -0.035), log=False)
            ratingText.setText(str(marker), log=False)
        
        # *slidersoru* updates
        if slidersoru.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            slidersoru.frameNStart = frameN  # exact frame index
            slidersoru.tStart = t  # local t and not account for scr refresh
            slidersoru.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slidersoru, 'tStartRefresh')  # time at next scr refresh
            slidersoru.setAutoDraw(True)
        if slidersoru.status == STARTED:  # only update if drawing
            slidersoru.setPos((0, 0.2), log=False)
        # *trialbitiren* updates
        if trialbitiren.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            trialbitiren.frameNStart = frameN  # exact frame index
            trialbitiren.tStart = t  # local t and not account for scr refresh
            trialbitiren.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialbitiren, 'tStartRefresh')  # time at next scr refresh
            trialbitiren.status = STARTED
            trialbitiren.mouseClock.reset()
            prevButtonState = trialbitiren.getPressed()  # if button is down already this ISN'T a new click
        if trialbitiren.status == STARTED:  # only update if started and not finished!
            buttons = trialbitiren.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bitti)
                        clickableList = bitti
                    except:
                        clickableList = [bitti]
                    for obj in clickableList:
                        if obj.contains(trialbitiren):
                            gotValidClick = True
                            trialbitiren.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *bitti* updates
        if bitti.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            bitti.frameNStart = frameN  # exact frame index
            bitti.tStart = t  # local t and not account for scr refresh
            bitti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitti, 'tStartRefresh')  # time at next scr refresh
            bitti.setAutoDraw(True)
        
        # *negatiftext* updates
        if negatiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            negatiftext.frameNStart = frameN  # exact frame index
            negatiftext.tStart = t  # local t and not account for scr refresh
            negatiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negatiftext, 'tStartRefresh')  # time at next scr refresh
            negatiftext.setAutoDraw(True)
        
        # *pozitiftext* updates
        if pozitiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            pozitiftext.frameNStart = frameN  # exact frame index
            pozitiftext.tStart = t  # local t and not account for scr refresh
            pozitiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pozitiftext, 'tStartRefresh')  # time at next scr refresh
            pozitiftext.setAutoDraw(True)
        
        # *notrtext* updates
        if notrtext.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            notrtext.frameNStart = frameN  # exact frame index
            notrtext.tStart = t  # local t and not account for scr refresh
            notrtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notrtext, 'tStartRefresh')  # time at next scr refresh
            notrtext.setAutoDraw(True)
        
        # *fakemarker_2* updates
        if fakemarker_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            fakemarker_2.frameNStart = frameN  # exact frame index
            fakemarker_2.tStart = t  # local t and not account for scr refresh
            fakemarker_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fakemarker_2, 'tStartRefresh')  # time at next scr refresh
            fakemarker_2.setAutoDraw(True)
        if fakemarker_2.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                fakemarker_2.tStop = t  # not accounting for scr refresh
                fakemarker_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fakemarker_2, 'tStopRefresh')  # time at next scr refresh
                fakemarker_2.setAutoDraw(False)
        
        # *arrows* updates
        if arrows.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            arrows.frameNStart = frameN  # exact frame index
            arrows.tStart = t  # local t and not account for scr refresh
            arrows.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows, 'tStartRefresh')  # time at next scr refresh
            arrows.setAutoDraw(True)
        if arrows.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                arrows.tStop = t  # not accounting for scr refresh
                arrows.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrows, 'tStopRefresh')  # time at next scr refresh
                arrows.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in duygularComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "duygular"-------
    for thisComponent in duygularComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duygu1.addData('slider.response', slider.getRating())
    duygu1.addData('slider.rt', slider.getRT())
    # store data for duygu1 (TrialHandler)
    # the Routine "duygular" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'duygu1'

# get names of stimulus parameters
if duygu1.trialList in ([], [None], None):
    params = []
else:
    params = duygu1.trialList[0].keys()
# save data for this loop
duygu1.saveAsExcel(filename + '.xlsx', sheetName='duygu1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
duygu1.saveAsText(filename + 'duygu1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
duygu3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='duygu3')
thisExp.addLoop(duygu3)  # add the loop to the experiment
thisDuygu3 = duygu3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDuygu3.rgb)
if thisDuygu3 != None:
    for paramName in thisDuygu3:
        exec('{} = thisDuygu3[paramName]'.format(paramName))

for thisDuygu3 in duygu3:
    currentLoop = duygu3
    # abbreviate parameter names if possible (e.g. rgb = thisDuygu3.rgb)
    if thisDuygu3 != None:
        for paramName in thisDuygu3:
            exec('{} = thisDuygu3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "duygular"-------
    continueRoutine = True
    # update component parameters for each repeat
    #yanda olması için exp değerleri: (0.55, -.095)
    thisPos = 0
    marker = slider.getMarkerPos()
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
        labels=("0", "10","20", "30", "40", "50", "60", "70", "80", "90", "100"), ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=5.0,
        style='rating', styleTweaks=(), opacity=1,
        color='black', fillColor='black', borderColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, depth=-1, readOnly=False)
    slider.marker = visual.Rect(
        win=win, name='polygon',units=None, 
        width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
        ori=0.0, pos=(0,-3),
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
        opacity=None, depth=-9.0, interpolate=True)
    slider.tickLines.opacities = 0
    slider.reset()
    # setup some python lists for storing info about the trialbitiren
    trialbitiren.clicked_name = []
    gotValidClick = False  # until a click is received
    bitti.setImage('tamam.png')
    negatiftext.setText(negatif)
    pozitiftext.setText(pozitif)
    notrtext.setText(notr)
    # keep track of which components have finished
    duygularComponents = [slider, ratingText, slidersoru, trialbitiren, bitti, negatiftext, pozitiftext, notrtext, fakemarker_2, arrows]
    for thisComponent in duygularComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    duygularClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "duygular"-------
    while continueRoutine:
        # get current time
        t = duygularClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=duygularClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if slider.getMarkerPos() != None:
            thisPos = (slider.getMarkerPos() / 100)-0.5
            marker = int(slider.getMarkerPos())
        else:
            marker = ""
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *ratingText* updates
        if ratingText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ratingText.frameNStart = frameN  # exact frame index
            ratingText.tStart = t  # local t and not account for scr refresh
            ratingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText, 'tStartRefresh')  # time at next scr refresh
            ratingText.setAutoDraw(True)
        if ratingText.status == STARTED:  # only update if drawing
            ratingText.setPos((thisPos, -0.035), log=False)
            ratingText.setText(str(marker), log=False)
        
        # *slidersoru* updates
        if slidersoru.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            slidersoru.frameNStart = frameN  # exact frame index
            slidersoru.tStart = t  # local t and not account for scr refresh
            slidersoru.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slidersoru, 'tStartRefresh')  # time at next scr refresh
            slidersoru.setAutoDraw(True)
        if slidersoru.status == STARTED:  # only update if drawing
            slidersoru.setPos((0, 0.2), log=False)
        # *trialbitiren* updates
        if trialbitiren.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            trialbitiren.frameNStart = frameN  # exact frame index
            trialbitiren.tStart = t  # local t and not account for scr refresh
            trialbitiren.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialbitiren, 'tStartRefresh')  # time at next scr refresh
            trialbitiren.status = STARTED
            trialbitiren.mouseClock.reset()
            prevButtonState = trialbitiren.getPressed()  # if button is down already this ISN'T a new click
        if trialbitiren.status == STARTED:  # only update if started and not finished!
            buttons = trialbitiren.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bitti)
                        clickableList = bitti
                    except:
                        clickableList = [bitti]
                    for obj in clickableList:
                        if obj.contains(trialbitiren):
                            gotValidClick = True
                            trialbitiren.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *bitti* updates
        if bitti.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            bitti.frameNStart = frameN  # exact frame index
            bitti.tStart = t  # local t and not account for scr refresh
            bitti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitti, 'tStartRefresh')  # time at next scr refresh
            bitti.setAutoDraw(True)
        
        # *negatiftext* updates
        if negatiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            negatiftext.frameNStart = frameN  # exact frame index
            negatiftext.tStart = t  # local t and not account for scr refresh
            negatiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negatiftext, 'tStartRefresh')  # time at next scr refresh
            negatiftext.setAutoDraw(True)
        
        # *pozitiftext* updates
        if pozitiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            pozitiftext.frameNStart = frameN  # exact frame index
            pozitiftext.tStart = t  # local t and not account for scr refresh
            pozitiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pozitiftext, 'tStartRefresh')  # time at next scr refresh
            pozitiftext.setAutoDraw(True)
        
        # *notrtext* updates
        if notrtext.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            notrtext.frameNStart = frameN  # exact frame index
            notrtext.tStart = t  # local t and not account for scr refresh
            notrtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notrtext, 'tStartRefresh')  # time at next scr refresh
            notrtext.setAutoDraw(True)
        
        # *fakemarker_2* updates
        if fakemarker_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            fakemarker_2.frameNStart = frameN  # exact frame index
            fakemarker_2.tStart = t  # local t and not account for scr refresh
            fakemarker_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fakemarker_2, 'tStartRefresh')  # time at next scr refresh
            fakemarker_2.setAutoDraw(True)
        if fakemarker_2.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                fakemarker_2.tStop = t  # not accounting for scr refresh
                fakemarker_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fakemarker_2, 'tStopRefresh')  # time at next scr refresh
                fakemarker_2.setAutoDraw(False)
        
        # *arrows* updates
        if arrows.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            arrows.frameNStart = frameN  # exact frame index
            arrows.tStart = t  # local t and not account for scr refresh
            arrows.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows, 'tStartRefresh')  # time at next scr refresh
            arrows.setAutoDraw(True)
        if arrows.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                arrows.tStop = t  # not accounting for scr refresh
                arrows.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrows, 'tStopRefresh')  # time at next scr refresh
                arrows.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in duygularComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "duygular"-------
    for thisComponent in duygularComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duygu3.addData('slider.response', slider.getRating())
    duygu3.addData('slider.rt', slider.getRT())
    # store data for duygu3 (TrialHandler)
    # the Routine "duygular" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'duygu3'

# get names of stimulus parameters
if duygu3.trialList in ([], [None], None):
    params = []
else:
    params = duygu3.trialList[0].keys()
# save data for this loop
duygu3.saveAsExcel(filename + '.xlsx', sheetName='duygu3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
duygu3.saveAsText(filename + 'duygu3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
subb = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='subb')
thisExp.addLoop(subb)  # add the loop to the experiment
thisSubb = subb.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSubb.rgb)
if thisSubb != None:
    for paramName in thisSubb:
        exec('{} = thisSubb[paramName]'.format(paramName))

for thisSubb in subb:
    currentLoop = subb
    # abbreviate parameter names if possible (e.g. rgb = thisSubb.rgb)
    if thisSubb != None:
        for paramName in thisSubb:
            exec('{} = thisSubb[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "subtracct"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    subtracctComponents = []
    for thisComponent in subtracctComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    subtracctClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "subtracct"-------
    while continueRoutine:
        # get current time
        t = subtracctClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=subtracctClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subtracctComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "subtracct"-------
    for thisComponent in subtracctComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duygufarksad = int(subtract(duygu1.data["slider.response"][0], duygu3.data["slider.response"][0]))
    subb.addData("duygu fark üzüntü", duygufarksad)
    
    subb.saveAsExcel(filename + '.xlsx', sheetName='subb',
        stimOut=params, dataOut=['all_raw'])
    # the Routine "subtracct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'subb'

# get names of stimulus parameters
if subb.trialList in ([], [None], None):
    params = []
else:
    params = subb.trialList[0].keys()
# save data for this loop
subb.saveAsExcel(filename + '.xlsx', sheetName='subb',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
subb.saveAsText(filename + 'subb.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
brsi1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bsri.xlsx'),
    seed=None, name='brsi1')
thisExp.addLoop(brsi1)  # add the loop to the experiment
thisBrsi1 = brsi1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBrsi1.rgb)
if thisBrsi1 != None:
    for paramName in thisBrsi1:
        exec('{} = thisBrsi1[paramName]'.format(paramName))

for thisBrsi1 in brsi1:
    currentLoop = brsi1
    # abbreviate parameter names if possible (e.g. rgb = thisBrsi1.rgb)
    if thisBrsi1 != None:
        for paramName in thisBrsi1:
            exec('{} = thisBrsi1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ruminasyon"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_2.reset()
    ruminasyonsorular.setText(itemText)
    # setup some python lists for storing info about the trialbitiren_2
    trialbitiren_2.clicked_name = []
    gotValidClick = False  # until a click is received
    thisPoss = 0
    markerr = ""
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
        labels=("0", "10","20", "30", "40", "50", "60", "70", "80", "90", "100"), ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=5.0,
        style='rating', styleTweaks=(), opacity=1,
        color='black', fillColor='black', borderColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, depth=-1, readOnly=False)
    slider_2.marker = visual.Rect(
        win=win, name='polygon',units=None, 
        width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
        ori=0.0, pos=(0,-3),
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
        opacity=None, depth=-9.0, interpolate=True)
    slider_2.tickLines.opacities = 0
    # keep track of which components have finished
    ruminasyonComponents = [slider_2, ruminasyonsorular, bitti_2, trialbitiren_2, ratingText_2, ruminasyonklvz, fakemarker_3, negatiftext_2, pozitiftext_2, arrows_2]
    for thisComponent in ruminasyonComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ruminasyonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ruminasyon"-------
    while continueRoutine:
        # get current time
        t = ruminasyonClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ruminasyonClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        
        # *ruminasyonsorular* updates
        if ruminasyonsorular.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ruminasyonsorular.frameNStart = frameN  # exact frame index
            ruminasyonsorular.tStart = t  # local t and not account for scr refresh
            ruminasyonsorular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ruminasyonsorular, 'tStartRefresh')  # time at next scr refresh
            ruminasyonsorular.setAutoDraw(True)
        
        # *bitti_2* updates
        if bitti_2.status == NOT_STARTED and markerr is not "":
            # keep track of start time/frame for later
            bitti_2.frameNStart = frameN  # exact frame index
            bitti_2.tStart = t  # local t and not account for scr refresh
            bitti_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitti_2, 'tStartRefresh')  # time at next scr refresh
            bitti_2.setAutoDraw(True)
        # *trialbitiren_2* updates
        if trialbitiren_2.status == NOT_STARTED and markerr is not "":
            # keep track of start time/frame for later
            trialbitiren_2.frameNStart = frameN  # exact frame index
            trialbitiren_2.tStart = t  # local t and not account for scr refresh
            trialbitiren_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialbitiren_2, 'tStartRefresh')  # time at next scr refresh
            trialbitiren_2.status = STARTED
            trialbitiren_2.mouseClock.reset()
            prevButtonState = trialbitiren_2.getPressed()  # if button is down already this ISN'T a new click
        if trialbitiren_2.status == STARTED:  # only update if started and not finished!
            buttons = trialbitiren_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bitti_2)
                        clickableList = bitti_2
                    except:
                        clickableList = [bitti_2]
                    for obj in clickableList:
                        if obj.contains(trialbitiren_2):
                            gotValidClick = True
                            trialbitiren_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        if slider_2.getMarkerPos() is None:
            thisPoss = 0
            markerr = ""
        else:
            thisPoss = (slider_2.getMarkerPos() / 100)-0.5
            markerr = int(slider_2.getMarkerPos())
        
        # *ratingText_2* updates
        if ratingText_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ratingText_2.frameNStart = frameN  # exact frame index
            ratingText_2.tStart = t  # local t and not account for scr refresh
            ratingText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText_2, 'tStartRefresh')  # time at next scr refresh
            ratingText_2.setAutoDraw(True)
        if ratingText_2.status == STARTED:  # only update if drawing
            ratingText_2.setPos((thisPoss, -.025), log=False)
            ratingText_2.setText(str(markerr), log=False)
        
        # *ruminasyonklvz* updates
        if ruminasyonklvz.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ruminasyonklvz.frameNStart = frameN  # exact frame index
            ruminasyonklvz.tStart = t  # local t and not account for scr refresh
            ruminasyonklvz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ruminasyonklvz, 'tStartRefresh')  # time at next scr refresh
            ruminasyonklvz.setAutoDraw(True)
        
        # *fakemarker_3* updates
        if fakemarker_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            fakemarker_3.frameNStart = frameN  # exact frame index
            fakemarker_3.tStart = t  # local t and not account for scr refresh
            fakemarker_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fakemarker_3, 'tStartRefresh')  # time at next scr refresh
            fakemarker_3.setAutoDraw(True)
        if fakemarker_3.status == STARTED:
            if bool(slider_2.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                fakemarker_3.tStop = t  # not accounting for scr refresh
                fakemarker_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fakemarker_3, 'tStopRefresh')  # time at next scr refresh
                fakemarker_3.setAutoDraw(False)
        
        # *negatiftext_2* updates
        if negatiftext_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            negatiftext_2.frameNStart = frameN  # exact frame index
            negatiftext_2.tStart = t  # local t and not account for scr refresh
            negatiftext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negatiftext_2, 'tStartRefresh')  # time at next scr refresh
            negatiftext_2.setAutoDraw(True)
        
        # *pozitiftext_2* updates
        if pozitiftext_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            pozitiftext_2.frameNStart = frameN  # exact frame index
            pozitiftext_2.tStart = t  # local t and not account for scr refresh
            pozitiftext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pozitiftext_2, 'tStartRefresh')  # time at next scr refresh
            pozitiftext_2.setAutoDraw(True)
        
        # *arrows_2* updates
        if arrows_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            arrows_2.frameNStart = frameN  # exact frame index
            arrows_2.tStart = t  # local t and not account for scr refresh
            arrows_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows_2, 'tStartRefresh')  # time at next scr refresh
            arrows_2.setAutoDraw(True)
        if arrows_2.status == STARTED:
            if bool(slider_2.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                arrows_2.tStop = t  # not accounting for scr refresh
                arrows_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrows_2, 'tStopRefresh')  # time at next scr refresh
                arrows_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ruminasyonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ruminasyon"-------
    for thisComponent in ruminasyonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    brsi1.addData('slider_2.response', slider_2.getRating())
    brsi1.addData('slider_2.rt', slider_2.getRT())
    # store data for brsi1 (TrialHandler)
    # the Routine "ruminasyon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'brsi1'

# get names of stimulus parameters
if brsi1.trialList in ([], [None], None):
    params = []
else:
    params = brsi1.trialList[0].keys()
# save data for this loop
brsi1.saveAsExcel(filename + '.xlsx', sheetName='brsi1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
brsi1.saveAsText(filename + 'brsi1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "session_end"-------
continueRoutine = True
# update component parameters for each repeat
telegram_send.send(messages=["Aşama sona erdi."])
# keep track of which components have finished
session_endComponents = []
for thisComponent in session_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
session_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "session_end"-------
while continueRoutine:
    # get current time
    t = session_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=session_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in session_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "session_end"-------
for thisComponent in session_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "session_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "navonbilgi"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
navonbilgiComponents = [colorblue_4, mouse_6, tamam4, orneknavonimg, text_3]
for thisComponent in navonbilgiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
navonbilgiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "navonbilgi"-------
while continueRoutine:
    # get current time
    t = navonbilgiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=navonbilgiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_4* updates
    if colorblue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_4.frameNStart = frameN  # exact frame index
        colorblue_4.tStart = t  # local t and not account for scr refresh
        colorblue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_4, 'tStartRefresh')  # time at next scr refresh
        colorblue_4.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamam4)
                    clickableList = tamam4
                except:
                    clickableList = [tamam4]
                for obj in clickableList:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamam4* updates
    if tamam4.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamam4.frameNStart = frameN  # exact frame index
        tamam4.tStart = t  # local t and not account for scr refresh
        tamam4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamam4, 'tStartRefresh')  # time at next scr refresh
        tamam4.setAutoDraw(True)
    
    # *orneknavonimg* updates
    if orneknavonimg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        orneknavonimg.frameNStart = frameN  # exact frame index
        orneknavonimg.tStart = t  # local t and not account for scr refresh
        orneknavonimg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(orneknavonimg, 'tStartRefresh')  # time at next scr refresh
        orneknavonimg.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in navonbilgiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "navonbilgi"-------
for thisComponent in navonbilgiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_6.getPos()
buttons = mouse_6.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamam4)
        clickableList = tamam4
    except:
        clickableList = [tamam4]
    for obj in clickableList:
        if obj.contains(mouse_6):
            gotValidClick = True
            mouse_6.clicked_name.append(obj.name)
thisExp.addData('mouse_6.x', x)
thisExp.addData('mouse_6.y', y)
thisExp.addData('mouse_6.leftButton', buttons[0])
thisExp.addData('mouse_6.midButton', buttons[1])
thisExp.addData('mouse_6.rightButton', buttons[2])
if len(mouse_6.clicked_name):
    thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
thisExp.addData('tamam4.started', tamam4.tStartRefresh)
thisExp.addData('tamam4.stopped', tamam4.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "navonbilgi" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
denemeloop = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='denemeloop')
thisExp.addLoop(denemeloop)  # add the loop to the experiment
thisDenemeloop = denemeloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDenemeloop.rgb)
if thisDenemeloop != None:
    for paramName in thisDenemeloop:
        exec('{} = thisDenemeloop[paramName]'.format(paramName))

for thisDenemeloop in denemeloop:
    currentLoop = denemeloop
    # abbreviate parameter names if possible (e.g. rgb = thisDenemeloop.rgb)
    if thisDenemeloop != None:
        for paramName in thisDenemeloop:
            exec('{} = thisDenemeloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(9.900000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [colorblue_8, text_2, text_5]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colorblue_8* updates
        if colorblue_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            colorblue_8.frameNStart = frameN  # exact frame index
            colorblue_8.tStart = t  # local t and not account for scr refresh
            colorblue_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colorblue_8, 'tStartRefresh')  # time at next scr refresh
            colorblue_8.setAutoDraw(True)
        if colorblue_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > colorblue_8.tStartRefresh + 9.9-frameTolerance:
                # keep track of stop time/frame for later
                colorblue_8.tStop = t  # not accounting for scr refresh
                colorblue_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(colorblue_8, 'tStopRefresh')  # time at next scr refresh
                colorblue_8.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 9.9-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 9.9-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        if text_5.status == STARTED:  # only update if drawing
            text_5.setText(str(round((10-t),1)), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    denemeloop.addData('text_5.started', text_5.tStartRefresh)
    denemeloop.addData('text_5.stopped', text_5.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    navon2deneme = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('navon2.xlsx'),
        seed=None, name='navon2deneme')
    thisExp.addLoop(navon2deneme)  # add the loop to the experiment
    thisNavon2deneme = navon2deneme.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNavon2deneme.rgb)
    if thisNavon2deneme != None:
        for paramName in thisNavon2deneme:
            exec('{} = thisNavon2deneme[paramName]'.format(paramName))
    
    for thisNavon2deneme in navon2deneme:
        currentLoop = navon2deneme
        # abbreviate parameter names if possible (e.g. rgb = thisNavon2deneme.rgb)
        if thisNavon2deneme != None:
            for paramName in thisNavon2deneme:
                exec('{} = thisNavon2deneme[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "navon_pilot"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        poseee=[-5,5]
        random_posee = random.choice(poseee)
        letter_2.setPos((random_posee, 0))
        letter_2.setImage(soru)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        noise_4.setPos((random_posee, 0))
        # keep track of which components have finished
        navon_pilotComponents = [letter_2, fix_2, key_resp_2, noise_4]
        for thisComponent in navon_pilotComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        navon_pilotClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "navon_pilot"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = navon_pilotClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=navon_pilotClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *letter_2* updates
            if letter_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                letter_2.frameNStart = frameN  # exact frame index
                letter_2.tStart = t  # local t and not account for scr refresh
                letter_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letter_2, 'tStartRefresh')  # time at next scr refresh
                letter_2.setAutoDraw(True)
            if letter_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > letter_2.tStartRefresh + 0.15-frameTolerance:
                    # keep track of stop time/frame for later
                    letter_2.tStop = t  # not accounting for scr refresh
                    letter_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(letter_2, 'tStopRefresh')  # time at next scr refresh
                    letter_2.setAutoDraw(False)
            
            # *fix_2* updates
            if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_2.frameNStart = frameN  # exact frame index
                fix_2.tStart = t  # local t and not account for scr refresh
                fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(True)
            if fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_2.tStop = t  # not accounting for scr refresh
                    fix_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                    fix_2.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(dogru)) or (key_resp_2.keys == dogru):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *noise_4* updates
            if noise_4.status == NOT_STARTED and tThisFlip >= 0.65-frameTolerance:
                # keep track of start time/frame for later
                noise_4.frameNStart = frameN  # exact frame index
                noise_4.tStart = t  # local t and not account for scr refresh
                noise_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_4, 'tStartRefresh')  # time at next scr refresh
                noise_4.setAutoDraw(True)
            if noise_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_4.tStartRefresh + 2.85-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_4.tStop = t  # not accounting for scr refresh
                    noise_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_4, 'tStopRefresh')  # time at next scr refresh
                    noise_4.setAutoDraw(False)
            if noise_4.status == STARTED:
                if noise_4._needBuild:
                    noise_4.buildNoise()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in navon_pilotComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "navon_pilot"-------
        for thisComponent in navon_pilotComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(dogru).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for navon2deneme (TrialHandler)
        navon2deneme.addData('key_resp_2.keys',key_resp_2.keys)
        navon2deneme.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            navon2deneme.addData('key_resp_2.rt', key_resp_2.rt)
        
        # ------Prepare to start Routine "dogru_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        dogrusu.setText(dogru)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        dogru_2Components = [dogrusu, texttt, key_resp_3]
        for thisComponent in dogru_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        dogru_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "dogru_2"-------
        while continueRoutine:
            # get current time
            t = dogru_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=dogru_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *dogrusu* updates
            if dogrusu.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dogrusu.frameNStart = frameN  # exact frame index
                dogrusu.tStart = t  # local t and not account for scr refresh
                dogrusu.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dogrusu, 'tStartRefresh')  # time at next scr refresh
                dogrusu.setAutoDraw(True)
            
            # *texttt* updates
            if texttt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                texttt.frameNStart = frameN  # exact frame index
                texttt.tStart = t  # local t and not account for scr refresh
                texttt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(texttt, 'tStartRefresh')  # time at next scr refresh
                texttt.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['right', 'left'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dogru_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "dogru_2"-------
        for thisComponent in dogru_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        navon2deneme.addData('texttt.started', texttt.tStartRefresh)
        navon2deneme.addData('texttt.stopped', texttt.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        navon2deneme.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            navon2deneme.addData('key_resp_3.rt', key_resp_3.rt)
        navon2deneme.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        navon2deneme.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "dogru_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'navon2deneme'
    
    # get names of stimulus parameters
    if navon2deneme.trialList in ([], [None], None):
        params = []
    else:
        params = navon2deneme.trialList[0].keys()
    # save data for this loop
    navon2deneme.saveAsExcel(filename + '.xlsx', sheetName='navon2deneme',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    navon2deneme.saveAsText(filename + 'navon2deneme.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "pilot_navon"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    pilot_navonComponents = [colorblue_7, pilotnavontxt, tamam4_2, tekrarbuttonimg, tekrarbutton, tamambutton, tekrartexttt]
    for thisComponent in pilot_navonComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pilot_navonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pilot_navon"-------
    while continueRoutine:
        # get current time
        t = pilot_navonClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pilot_navonClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colorblue_7* updates
        if colorblue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            colorblue_7.frameNStart = frameN  # exact frame index
            colorblue_7.tStart = t  # local t and not account for scr refresh
            colorblue_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colorblue_7, 'tStartRefresh')  # time at next scr refresh
            colorblue_7.setAutoDraw(True)
        
        # *pilotnavontxt* updates
        if pilotnavontxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pilotnavontxt.frameNStart = frameN  # exact frame index
            pilotnavontxt.tStart = t  # local t and not account for scr refresh
            pilotnavontxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pilotnavontxt, 'tStartRefresh')  # time at next scr refresh
            pilotnavontxt.setAutoDraw(True)
        
        # *tamam4_2* updates
        if tamam4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tamam4_2.frameNStart = frameN  # exact frame index
            tamam4_2.tStart = t  # local t and not account for scr refresh
            tamam4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tamam4_2, 'tStartRefresh')  # time at next scr refresh
            tamam4_2.setAutoDraw(True)
        
        # *tekrarbuttonimg* updates
        if tekrarbuttonimg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tekrarbuttonimg.frameNStart = frameN  # exact frame index
            tekrarbuttonimg.tStart = t  # local t and not account for scr refresh
            tekrarbuttonimg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tekrarbuttonimg, 'tStartRefresh')  # time at next scr refresh
            tekrarbuttonimg.setAutoDraw(True)
        
        # *tekrarbutton* updates
        if tekrarbutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tekrarbutton.frameNStart = frameN  # exact frame index
            tekrarbutton.tStart = t  # local t and not account for scr refresh
            tekrarbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tekrarbutton, 'tStartRefresh')  # time at next scr refresh
            tekrarbutton.setAutoDraw(True)
        if tekrarbutton.status == STARTED:
            # check whether tekrarbutton has been pressed
            if tekrarbutton.isClicked:
                if not tekrarbutton.wasClicked:
                    tekrarbutton.timesOn.append(tekrarbutton.buttonClock.getTime()) # store time of first click
                    tekrarbutton.timesOff.append(tekrarbutton.buttonClock.getTime()) # store time clicked until
                else:
                    tekrarbutton.timesOff[-1] = tekrarbutton.buttonClock.getTime() # update time clicked until
                if not tekrarbutton.wasClicked:
                    continueRoutine = False  # end routine when tekrarbutton is clicked
                    None
                tekrarbutton.wasClicked = True  # if tekrarbutton is still clicked next frame, it is not a new click
            else:
                tekrarbutton.wasClicked = False  # if tekrarbutton is clicked next frame, it is a new click
        else:
            tekrarbutton.wasClicked = False  # if tekrarbutton is clicked next frame, it is a new click
        
        # *tamambutton* updates
        if tamambutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tamambutton.frameNStart = frameN  # exact frame index
            tamambutton.tStart = t  # local t and not account for scr refresh
            tamambutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tamambutton, 'tStartRefresh')  # time at next scr refresh
            tamambutton.setAutoDraw(True)
        if tamambutton.status == STARTED:
            # check whether tamambutton has been pressed
            if tamambutton.isClicked:
                if not tamambutton.wasClicked:
                    tamambutton.timesOn.append(tamambutton.buttonClock.getTime()) # store time of first click
                    tamambutton.timesOff.append(tamambutton.buttonClock.getTime()) # store time clicked until
                else:
                    tamambutton.timesOff[-1] = tamambutton.buttonClock.getTime() # update time clicked until
                if not tamambutton.wasClicked:
                    continueRoutine = False  # end routine when tamambutton is clicked
                    denemeloop.finished = True
                tamambutton.wasClicked = True  # if tamambutton is still clicked next frame, it is not a new click
            else:
                tamambutton.wasClicked = False  # if tamambutton is clicked next frame, it is a new click
        else:
            tamambutton.wasClicked = False  # if tamambutton is clicked next frame, it is a new click
        
        # *tekrartexttt* updates
        if tekrartexttt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tekrartexttt.frameNStart = frameN  # exact frame index
            tekrartexttt.tStart = t  # local t and not account for scr refresh
            tekrartexttt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tekrartexttt, 'tStartRefresh')  # time at next scr refresh
            tekrartexttt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pilot_navonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pilot_navon"-------
    for thisComponent in pilot_navonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    denemeloop.addData('tekrarbuttonimg.started', tekrarbuttonimg.tStartRefresh)
    denemeloop.addData('tekrarbuttonimg.stopped', tekrarbuttonimg.tStopRefresh)
    denemeloop.addData('tekrarbutton.started', tekrarbutton.tStartRefresh)
    denemeloop.addData('tekrarbutton.stopped', tekrarbutton.tStopRefresh)
    denemeloop.addData('tekrarbutton.numClicks', tekrarbutton.numClicks)
    if tekrarbutton.numClicks:
       denemeloop.addData('tekrarbutton.timesOn', tekrarbutton.timesOn)
       denemeloop.addData('tekrarbutton.timesOff', tekrarbutton.timesOff)
    else:
       denemeloop.addData('tekrarbutton.timesOn', "")
       denemeloop.addData('tekrarbutton.timesOff', "")
    denemeloop.addData('tamambutton.started', tamambutton.tStartRefresh)
    denemeloop.addData('tamambutton.stopped', tamambutton.tStopRefresh)
    denemeloop.addData('tamambutton.numClicks', tamambutton.numClicks)
    if tamambutton.numClicks:
       denemeloop.addData('tamambutton.timesOn', tamambutton.timesOn)
       denemeloop.addData('tamambutton.timesOff', tamambutton.timesOff)
    else:
       denemeloop.addData('tamambutton.timesOn', "")
       denemeloop.addData('tamambutton.timesOff', "")
    denemeloop.addData('tekrartexttt.started', tekrartexttt.tStartRefresh)
    denemeloop.addData('tekrartexttt.stopped', tekrartexttt.tStopRefresh)
    # the Routine "pilot_navon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'denemeloop'

# get names of stimulus parameters
if denemeloop.trialList in ([], [None], None):
    params = []
else:
    params = denemeloop.trialList[0].keys()
# save data for this loop
denemeloop.saveAsExcel(filename + '.xlsx', sheetName='denemeloop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
denemeloop.saveAsText(filename + 'denemeloop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(9.900000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [colorblue_8, text_2, text_5]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_8* updates
    if colorblue_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_8.frameNStart = frameN  # exact frame index
        colorblue_8.tStart = t  # local t and not account for scr refresh
        colorblue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_8, 'tStartRefresh')  # time at next scr refresh
        colorblue_8.setAutoDraw(True)
    if colorblue_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > colorblue_8.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            colorblue_8.tStop = t  # not accounting for scr refresh
            colorblue_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(colorblue_8, 'tStopRefresh')  # time at next scr refresh
            colorblue_8.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    if text_5.status == STARTED:  # only update if drawing
        text_5.setText(str(round((10-t),1)), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
navonblok1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('navon.xlsx', selection='0:20'),
    seed=None, name='navonblok1')
thisExp.addLoop(navonblok1)  # add the loop to the experiment
thisNavonblok1 = navonblok1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNavonblok1.rgb)
if thisNavonblok1 != None:
    for paramName in thisNavonblok1:
        exec('{} = thisNavonblok1[paramName]'.format(paramName))

for thisNavonblok1 in navonblok1:
    currentLoop = navonblok1
    # abbreviate parameter names if possible (e.g. rgb = thisNavonblok1.rgb)
    if thisNavonblok1 != None:
        for paramName in thisNavonblok1:
            exec('{} = thisNavonblok1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "navon_1"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    letter.setPos((navonpose, 0))
    letter.setImage(soru)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    noise.setPos((navonpose, 0))
    # keep track of which components have finished
    navon_1Components = [letter, fix, key_resp, noise]
    for thisComponent in navon_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    navon_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "navon_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = navon_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=navon_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letter* updates
        if letter.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            letter.frameNStart = frameN  # exact frame index
            letter.tStart = t  # local t and not account for scr refresh
            letter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter, 'tStartRefresh')  # time at next scr refresh
            letter.setAutoDraw(True)
        if letter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                letter.tStop = t  # not accounting for scr refresh
                letter.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter, 'tStopRefresh')  # time at next scr refresh
                letter.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noise* updates
        if noise.status == NOT_STARTED and tThisFlip >= 0.65-frameTolerance:
            # keep track of start time/frame for later
            noise.frameNStart = frameN  # exact frame index
            noise.tStart = t  # local t and not account for scr refresh
            noise.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
            noise.setAutoDraw(True)
        if noise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise.tStartRefresh + 2.85-frameTolerance:
                # keep track of stop time/frame for later
                noise.tStop = t  # not accounting for scr refresh
                noise.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                noise.setAutoDraw(False)
        if noise.status == STARTED:
            if noise._needBuild:
                noise.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in navon_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "navon_1"-------
    for thisComponent in navon_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    navonblok1.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        navonblok1.addData('key_resp.rt', key_resp.rt)
    if key_resp.keys==correctAns:
        navonblok1.addData('correct',1);
    elif correctAns==None:
        navonblok1.addData('correct',1);
    else:
        navonblok1.addData('correct',0)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'navonblok1'

# get names of stimulus parameters
if navonblok1.trialList in ([], [None], None):
    params = []
else:
    params = navonblok1.trialList[0].keys()
# save data for this loop
navonblok1.saveAsExcel(filename + '.xlsx', sheetName='navonblok1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
navonblok1.saveAsText(filename + 'navonblok1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "interval"-------
continueRoutine = True
routineTimer.add(59.900000)
# update component parameters for each repeat
line_lenght = 30
# keep track of which components have finished
intervalComponents = [countdown, timer_line, mola]
for thisComponent in intervalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "interval"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intervalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intervalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *countdown* updates
    if countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        countdown.frameNStart = frameN  # exact frame index
        countdown.tStart = t  # local t and not account for scr refresh
        countdown.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown, 'tStartRefresh')  # time at next scr refresh
        countdown.setAutoDraw(True)
    if countdown.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            countdown.tStop = t  # not accounting for scr refresh
            countdown.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown, 'tStopRefresh')  # time at next scr refresh
            countdown.setAutoDraw(False)
    if countdown.status == STARTED:  # only update if drawing
        countdown.setText(round(60-t, ndigits=1), log=False)
    line_lenght = (30-(t/2))
    
    # *timer_line* updates
    if timer_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        timer_line.frameNStart = frameN  # exact frame index
        timer_line.tStart = t  # local t and not account for scr refresh
        timer_line.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(timer_line, 'tStartRefresh')  # time at next scr refresh
        timer_line.setAutoDraw(True)
    if timer_line.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > timer_line.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            timer_line.tStop = t  # not accounting for scr refresh
            timer_line.frameNStop = frameN  # exact frame index
            win.timeOnFlip(timer_line, 'tStopRefresh')  # time at next scr refresh
            timer_line.setAutoDraw(False)
    if timer_line.status == STARTED:  # only update if drawing
        timer_line.setSize((line_lenght, 1), log=False)
    
    # *mola* updates
    if mola.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mola.frameNStart = frameN  # exact frame index
        mola.tStart = t  # local t and not account for scr refresh
        mola.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mola, 'tStartRefresh')  # time at next scr refresh
        mola.setAutoDraw(True)
    if mola.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mola.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            mola.tStop = t  # not accounting for scr refresh
            mola.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mola, 'tStopRefresh')  # time at next scr refresh
            mola.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "interval"-------
for thisComponent in intervalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mola.started', mola.tStartRefresh)
thisExp.addData('mola.stopped', mola.tStopRefresh)

# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(9.900000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [colorblue_8, text_2, text_5]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_8* updates
    if colorblue_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_8.frameNStart = frameN  # exact frame index
        colorblue_8.tStart = t  # local t and not account for scr refresh
        colorblue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_8, 'tStartRefresh')  # time at next scr refresh
        colorblue_8.setAutoDraw(True)
    if colorblue_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > colorblue_8.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            colorblue_8.tStop = t  # not accounting for scr refresh
            colorblue_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(colorblue_8, 'tStopRefresh')  # time at next scr refresh
            colorblue_8.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    if text_5.status == STARTED:  # only update if drawing
        text_5.setText(str(round((10-t),1)), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
navonblok2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('navon.xlsx', selection='0:20'),
    seed=None, name='navonblok2')
thisExp.addLoop(navonblok2)  # add the loop to the experiment
thisNavonblok2 = navonblok2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNavonblok2.rgb)
if thisNavonblok2 != None:
    for paramName in thisNavonblok2:
        exec('{} = thisNavonblok2[paramName]'.format(paramName))

for thisNavonblok2 in navonblok2:
    currentLoop = navonblok2
    # abbreviate parameter names if possible (e.g. rgb = thisNavonblok2.rgb)
    if thisNavonblok2 != None:
        for paramName in thisNavonblok2:
            exec('{} = thisNavonblok2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "navon_2"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    letter_3.setPos((navonpose, 0))
    letter_3.setImage(soru)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    noise_5.setPos((navonpose, 0))
    # keep track of which components have finished
    navon_2Components = [letter_3, fix_3, key_resp_5, noise_5]
    for thisComponent in navon_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    navon_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "navon_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = navon_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=navon_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letter_3* updates
        if letter_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            letter_3.frameNStart = frameN  # exact frame index
            letter_3.tStart = t  # local t and not account for scr refresh
            letter_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter_3, 'tStartRefresh')  # time at next scr refresh
            letter_3.setAutoDraw(True)
        if letter_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter_3.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                letter_3.tStop = t  # not accounting for scr refresh
                letter_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter_3, 'tStopRefresh')  # time at next scr refresh
                letter_3.setAutoDraw(False)
        
        # *fix_3* updates
        if fix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_3.frameNStart = frameN  # exact frame index
            fix_3.tStart = t  # local t and not account for scr refresh
            fix_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_3, 'tStartRefresh')  # time at next scr refresh
            fix_3.setAutoDraw(True)
        if fix_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_3.tStop = t  # not accounting for scr refresh
                fix_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_3, 'tStopRefresh')  # time at next scr refresh
                fix_3.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noise_5* updates
        if noise_5.status == NOT_STARTED and tThisFlip >= 0.65-frameTolerance:
            # keep track of start time/frame for later
            noise_5.frameNStart = frameN  # exact frame index
            noise_5.tStart = t  # local t and not account for scr refresh
            noise_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_5, 'tStartRefresh')  # time at next scr refresh
            noise_5.setAutoDraw(True)
        if noise_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_5.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                noise_5.tStop = t  # not accounting for scr refresh
                noise_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_5, 'tStopRefresh')  # time at next scr refresh
                noise_5.setAutoDraw(False)
        if noise_5.status == STARTED:
            if noise_5._needBuild:
                noise_5.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in navon_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "navon_2"-------
    for thisComponent in navon_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    navonblok2.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        navonblok2.addData('key_resp_5.rt', key_resp_5.rt)
    if key_resp_5.keys==correctAns:
        navonblok2.addData('correct',1);
    elif correctAns==None:
        navonblok2.addData('correct',1);
    else:
        navonblok2.addData('correct',0)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'navonblok2'

# get names of stimulus parameters
if navonblok2.trialList in ([], [None], None):
    params = []
else:
    params = navonblok2.trialList[0].keys()
# save data for this loop
navonblok2.saveAsExcel(filename + '.xlsx', sheetName='navonblok2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
navonblok2.saveAsText(filename + 'navonblok2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "session_end"-------
continueRoutine = True
# update component parameters for each repeat
telegram_send.send(messages=["Aşama sona erdi."])
# keep track of which components have finished
session_endComponents = []
for thisComponent in session_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
session_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "session_end"-------
while continueRoutine:
    # get current time
    t = session_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=session_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in session_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "session_end"-------
for thisComponent in session_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "session_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "cattellbilgi"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_7
mouse_7.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
cattellbilgiComponents = [colorblue_5, mouse_7, tamam5, cattelllbilgitxt1]
for thisComponent in cattellbilgiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
cattellbilgiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "cattellbilgi"-------
while continueRoutine:
    # get current time
    t = cattellbilgiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=cattellbilgiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_5* updates
    if colorblue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_5.frameNStart = frameN  # exact frame index
        colorblue_5.tStart = t  # local t and not account for scr refresh
        colorblue_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_5, 'tStartRefresh')  # time at next scr refresh
        colorblue_5.setAutoDraw(True)
    # *mouse_7* updates
    if mouse_7.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        mouse_7.frameNStart = frameN  # exact frame index
        mouse_7.tStart = t  # local t and not account for scr refresh
        mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
        mouse_7.status = STARTED
        mouse_7.mouseClock.reset()
        prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
    if mouse_7.status == STARTED:  # only update if started and not finished!
        buttons = mouse_7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamam5)
                    clickableList = tamam5
                except:
                    clickableList = [tamam5]
                for obj in clickableList:
                    if obj.contains(mouse_7):
                        gotValidClick = True
                        mouse_7.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamam5* updates
    if tamam5.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamam5.frameNStart = frameN  # exact frame index
        tamam5.tStart = t  # local t and not account for scr refresh
        tamam5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamam5, 'tStartRefresh')  # time at next scr refresh
        tamam5.setAutoDraw(True)
    
    # *cattelllbilgitxt1* updates
    if cattelllbilgitxt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cattelllbilgitxt1.frameNStart = frameN  # exact frame index
        cattelllbilgitxt1.tStart = t  # local t and not account for scr refresh
        cattelllbilgitxt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cattelllbilgitxt1, 'tStartRefresh')  # time at next scr refresh
        cattelllbilgitxt1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cattellbilgiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cattellbilgi"-------
for thisComponent in cattellbilgiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_7.getPos()
buttons = mouse_7.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamam5)
        clickableList = tamam5
    except:
        clickableList = [tamam5]
    for obj in clickableList:
        if obj.contains(mouse_7):
            gotValidClick = True
            mouse_7.clicked_name.append(obj.name)
thisExp.addData('mouse_7.x', x)
thisExp.addData('mouse_7.y', y)
thisExp.addData('mouse_7.leftButton', buttons[0])
thisExp.addData('mouse_7.midButton', buttons[1])
thisExp.addData('mouse_7.rightButton', buttons[2])
if len(mouse_7.clicked_name):
    thisExp.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
thisExp.addData('mouse_7.started', mouse_7.tStart)
thisExp.addData('mouse_7.stopped', mouse_7.tStop)
thisExp.nextEntry()
thisExp.addData('tamam5.started', tamam5.tStartRefresh)
thisExp.addData('tamam5.stopped', tamam5.tStopRefresh)
thisExp.addData('cattelllbilgitxt1.started', cattelllbilgitxt1.tStartRefresh)
thisExp.addData('cattelllbilgitxt1.stopped', cattelllbilgitxt1.tStopRefresh)
# the Routine "cattellbilgi" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
cattelll = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cattellfalse.xlsx', selection='0:7'),
    seed=None, name='cattelll')
thisExp.addLoop(cattelll)  # add the loop to the experiment
thisCattelll = cattelll.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCattelll.rgb)
if thisCattelll != None:
    for paramName in thisCattelll:
        exec('{} = thisCattelll[paramName]'.format(paramName))

for thisCattelll in cattelll:
    currentLoop = cattelll
    # abbreviate parameter names if possible (e.g. rgb = thisCattelll.rgb)
    if thisCattelll != None:
        for paramName in thisCattelll:
            exec('{} = thisCattelll[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cattell6"-------
    continueRoutine = True
    # update component parameters for each repeat
    ornek.setPos(pose)
    ornek.setSize(size)
    ornek.setImage(soru)
    a.setImage(cevapA)
    b.setImage(cevapB)
    c.setImage(cevapC)
    d.setImage(cevapD)
    e.setImage(cevapE)
    f.setImage(cevapF)
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    instructionn.setPos(poses)
    instructionn.setText(instruction)
    noise_2.setPos(pose2)
    timeuptext.setPos(pose2)
    # keep track of which components have finished
    cattell6Components = [ornek, a, b, c, d, e, f, mouse, instructionn, süre, noise_2, timeuptext]
    for thisComponent in cattell6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cattell6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cattell6"-------
    while continueRoutine:
        # get current time
        t = cattell6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cattell6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ornek* updates
        if ornek.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ornek.frameNStart = frameN  # exact frame index
            ornek.tStart = t  # local t and not account for scr refresh
            ornek.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ornek, 'tStartRefresh')  # time at next scr refresh
            ornek.setAutoDraw(True)
        
        # *a* updates
        if a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a.frameNStart = frameN  # exact frame index
            a.tStart = t  # local t and not account for scr refresh
            a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a, 'tStartRefresh')  # time at next scr refresh
            a.setAutoDraw(True)
        
        # *b* updates
        if b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b.frameNStart = frameN  # exact frame index
            b.tStart = t  # local t and not account for scr refresh
            b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b, 'tStartRefresh')  # time at next scr refresh
            b.setAutoDraw(True)
        
        # *c* updates
        if c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c.frameNStart = frameN  # exact frame index
            c.tStart = t  # local t and not account for scr refresh
            c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c, 'tStartRefresh')  # time at next scr refresh
            c.setAutoDraw(True)
        
        # *d* updates
        if d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            d.frameNStart = frameN  # exact frame index
            d.tStart = t  # local t and not account for scr refresh
            d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(d, 'tStartRefresh')  # time at next scr refresh
            d.setAutoDraw(True)
        
        # *e* updates
        if e.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            e.frameNStart = frameN  # exact frame index
            e.tStart = t  # local t and not account for scr refresh
            e.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(e, 'tStartRefresh')  # time at next scr refresh
            e.setAutoDraw(True)
        
        # *f* updates
        if f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            f.frameNStart = frameN  # exact frame index
            f.tStart = t  # local t and not account for scr refresh
            f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(f, 'tStartRefresh')  # time at next scr refresh
            f.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([a, b, c, d, e, f])
                        clickableList = [a, b, c, d, e, f]
                    except:
                        clickableList = [[a, b, c, d, e, f]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *instructionn* updates
        if instructionn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionn.frameNStart = frameN  # exact frame index
            instructionn.tStart = t  # local t and not account for scr refresh
            instructionn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionn, 'tStartRefresh')  # time at next scr refresh
            instructionn.setAutoDraw(True)
        
        # *süre* updates
        if süre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            süre.frameNStart = frameN  # exact frame index
            süre.tStart = t  # local t and not account for scr refresh
            süre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(süre, 'tStartRefresh')  # time at next scr refresh
            süre.setAutoDraw(True)
        if süre.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 30-frameTolerance:
                # keep track of stop time/frame for later
                süre.tStop = t  # not accounting for scr refresh
                süre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(süre, 'tStopRefresh')  # time at next scr refresh
                süre.setAutoDraw(False)
        if süre.status == STARTED:  # only update if drawing
            süre.setText("Kalan süre: {0}".format(int(30-t)), log=False)
        
        # *noise_2* updates
        if noise_2.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            noise_2.frameNStart = frameN  # exact frame index
            noise_2.tStart = t  # local t and not account for scr refresh
            noise_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_2, 'tStartRefresh')  # time at next scr refresh
            noise_2.setAutoDraw(True)
        if noise_2.status == STARTED:
            if noise_2._needBuild:
                noise_2.buildNoise()
        
        # *timeuptext* updates
        if timeuptext.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            timeuptext.frameNStart = frameN  # exact frame index
            timeuptext.tStart = t  # local t and not account for scr refresh
            timeuptext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeuptext, 'tStartRefresh')  # time at next scr refresh
            timeuptext.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cattell6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cattell6"-------
    for thisComponent in cattell6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    cattelll.addData('a.started', a.tStartRefresh)
    cattelll.addData('a.stopped', a.tStopRefresh)
    cattelll.addData('b.started', b.tStartRefresh)
    cattelll.addData('b.stopped', b.tStopRefresh)
    cattelll.addData('c.started', c.tStartRefresh)
    cattelll.addData('c.stopped', c.tStopRefresh)
    cattelll.addData('d.started', d.tStartRefresh)
    cattelll.addData('d.stopped', d.tStopRefresh)
    cattelll.addData('e.started', e.tStartRefresh)
    cattelll.addData('e.stopped', e.tStopRefresh)
    cattelll.addData('f.started', f.tStartRefresh)
    cattelll.addData('f.stopped', f.tStopRefresh)
    # store data for cattelll (TrialHandler)
    # the Routine "cattell6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    soundd.setSound(correct, secs=1, hamming=True)
    soundd.setVolume(1.0, log=False)
    feedback_text.setText(correct_text)
    # keep track of which components have finished
    feedbackComponents = [soundd, feedback_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop soundd
        if soundd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            soundd.frameNStart = frameN  # exact frame index
            soundd.tStart = t  # local t and not account for scr refresh
            soundd.tStartRefresh = tThisFlipGlobal  # on global time
            soundd.play(when=win)  # sync with win flip
        if soundd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > soundd.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                soundd.tStop = t  # not accounting for scr refresh
                soundd.frameNStop = frameN  # exact frame index
                win.timeOnFlip(soundd, 'tStopRefresh')  # time at next scr refresh
                soundd.stop()
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    soundd.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'cattelll'

# get names of stimulus parameters
if cattelll.trialList in ([], [None], None):
    params = []
else:
    params = cattelll.trialList[0].keys()
# save data for this loop
cattelll.saveAsExcel(filename + '.xlsx', sheetName='cattelll',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
cattelll.saveAsText(filename + 'cattelll.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
cattell2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cattell2false.xlsx'),
    seed=None, name='cattell2')
thisExp.addLoop(cattell2)  # add the loop to the experiment
thisCattell2 = cattell2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCattell2.rgb)
if thisCattell2 != None:
    for paramName in thisCattell2:
        exec('{} = thisCattell2[paramName]'.format(paramName))

for thisCattell2 in cattell2:
    currentLoop = cattell2
    # abbreviate parameter names if possible (e.g. rgb = thisCattell2.rgb)
    if thisCattell2 != None:
        for paramName in thisCattell2:
            exec('{} = thisCattell2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cattell2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    harfsoru.setText(soru_catell)
    butoncvp_1.setText(cvp1)
    butoncvp_2.setText(cvp2)
    butoncvp_3.setText(cvp3)
    butoncvp_4.setText(cvp4)
    butoncvp_5.setText(cvp5)
    timeuptext_2.setPos((0, -1))
    # keep track of which components have finished
    cattell2_2Components = [harfsoru, kılavuz, butoncvp_1, butoncvp_2, butoncvp_3, butoncvp_4, butoncvp_5, noise_3, süre_2, timeuptext_2]
    for thisComponent in cattell2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cattell2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cattell2_2"-------
    while continueRoutine:
        # get current time
        t = cattell2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cattell2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *harfsoru* updates
        if harfsoru.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            harfsoru.frameNStart = frameN  # exact frame index
            harfsoru.tStart = t  # local t and not account for scr refresh
            harfsoru.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(harfsoru, 'tStartRefresh')  # time at next scr refresh
            harfsoru.setAutoDraw(True)
        
        # *kılavuz* updates
        if kılavuz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            kılavuz.frameNStart = frameN  # exact frame index
            kılavuz.tStart = t  # local t and not account for scr refresh
            kılavuz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kılavuz, 'tStartRefresh')  # time at next scr refresh
            kılavuz.setAutoDraw(True)
        
        # *butoncvp_1* updates
        if butoncvp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            butoncvp_1.frameNStart = frameN  # exact frame index
            butoncvp_1.tStart = t  # local t and not account for scr refresh
            butoncvp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(butoncvp_1, 'tStartRefresh')  # time at next scr refresh
            butoncvp_1.setAutoDraw(True)
        if butoncvp_1.status == STARTED:
            # check whether butoncvp_1 has been pressed
            if butoncvp_1.isClicked:
                if not butoncvp_1.wasClicked:
                    butoncvp_1.timesOn.append(butoncvp_1.buttonClock.getTime()) # store time of first click
                    butoncvp_1.timesOff.append(butoncvp_1.buttonClock.getTime()) # store time clicked until
                else:
                    butoncvp_1.timesOff[-1] = butoncvp_1.buttonClock.getTime() # update time clicked until
                if not butoncvp_1.wasClicked:
                    continueRoutine = False  # end routine when butoncvp_1 is clicked
                    None
                butoncvp_1.wasClicked = True  # if butoncvp_1 is still clicked next frame, it is not a new click
            else:
                butoncvp_1.wasClicked = False  # if butoncvp_1 is clicked next frame, it is a new click
        else:
            butoncvp_1.wasClicked = False  # if butoncvp_1 is clicked next frame, it is a new click
        
        # *butoncvp_2* updates
        if butoncvp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            butoncvp_2.frameNStart = frameN  # exact frame index
            butoncvp_2.tStart = t  # local t and not account for scr refresh
            butoncvp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(butoncvp_2, 'tStartRefresh')  # time at next scr refresh
            butoncvp_2.setAutoDraw(True)
        if butoncvp_2.status == STARTED:
            # check whether butoncvp_2 has been pressed
            if butoncvp_2.isClicked:
                if not butoncvp_2.wasClicked:
                    butoncvp_2.timesOn.append(butoncvp_2.buttonClock.getTime()) # store time of first click
                    butoncvp_2.timesOff.append(butoncvp_2.buttonClock.getTime()) # store time clicked until
                else:
                    butoncvp_2.timesOff[-1] = butoncvp_2.buttonClock.getTime() # update time clicked until
                if not butoncvp_2.wasClicked:
                    continueRoutine = False  # end routine when butoncvp_2 is clicked
                    None
                butoncvp_2.wasClicked = True  # if butoncvp_2 is still clicked next frame, it is not a new click
            else:
                butoncvp_2.wasClicked = False  # if butoncvp_2 is clicked next frame, it is a new click
        else:
            butoncvp_2.wasClicked = False  # if butoncvp_2 is clicked next frame, it is a new click
        
        # *butoncvp_3* updates
        if butoncvp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            butoncvp_3.frameNStart = frameN  # exact frame index
            butoncvp_3.tStart = t  # local t and not account for scr refresh
            butoncvp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(butoncvp_3, 'tStartRefresh')  # time at next scr refresh
            butoncvp_3.setAutoDraw(True)
        if butoncvp_3.status == STARTED:
            # check whether butoncvp_3 has been pressed
            if butoncvp_3.isClicked:
                if not butoncvp_3.wasClicked:
                    butoncvp_3.timesOn.append(butoncvp_3.buttonClock.getTime()) # store time of first click
                    butoncvp_3.timesOff.append(butoncvp_3.buttonClock.getTime()) # store time clicked until
                else:
                    butoncvp_3.timesOff[-1] = butoncvp_3.buttonClock.getTime() # update time clicked until
                if not butoncvp_3.wasClicked:
                    continueRoutine = False  # end routine when butoncvp_3 is clicked
                    None
                butoncvp_3.wasClicked = True  # if butoncvp_3 is still clicked next frame, it is not a new click
            else:
                butoncvp_3.wasClicked = False  # if butoncvp_3 is clicked next frame, it is a new click
        else:
            butoncvp_3.wasClicked = False  # if butoncvp_3 is clicked next frame, it is a new click
        
        # *butoncvp_4* updates
        if butoncvp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            butoncvp_4.frameNStart = frameN  # exact frame index
            butoncvp_4.tStart = t  # local t and not account for scr refresh
            butoncvp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(butoncvp_4, 'tStartRefresh')  # time at next scr refresh
            butoncvp_4.setAutoDraw(True)
        if butoncvp_4.status == STARTED:
            # check whether butoncvp_4 has been pressed
            if butoncvp_4.isClicked:
                if not butoncvp_4.wasClicked:
                    butoncvp_4.timesOn.append(butoncvp_4.buttonClock.getTime()) # store time of first click
                    butoncvp_4.timesOff.append(butoncvp_4.buttonClock.getTime()) # store time clicked until
                else:
                    butoncvp_4.timesOff[-1] = butoncvp_4.buttonClock.getTime() # update time clicked until
                if not butoncvp_4.wasClicked:
                    continueRoutine = False  # end routine when butoncvp_4 is clicked
                    None
                butoncvp_4.wasClicked = True  # if butoncvp_4 is still clicked next frame, it is not a new click
            else:
                butoncvp_4.wasClicked = False  # if butoncvp_4 is clicked next frame, it is a new click
        else:
            butoncvp_4.wasClicked = False  # if butoncvp_4 is clicked next frame, it is a new click
        
        # *butoncvp_5* updates
        if butoncvp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            butoncvp_5.frameNStart = frameN  # exact frame index
            butoncvp_5.tStart = t  # local t and not account for scr refresh
            butoncvp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(butoncvp_5, 'tStartRefresh')  # time at next scr refresh
            butoncvp_5.setAutoDraw(True)
        if butoncvp_5.status == STARTED:
            # check whether butoncvp_5 has been pressed
            if butoncvp_5.isClicked:
                if not butoncvp_5.wasClicked:
                    butoncvp_5.timesOn.append(butoncvp_5.buttonClock.getTime()) # store time of first click
                    butoncvp_5.timesOff.append(butoncvp_5.buttonClock.getTime()) # store time clicked until
                else:
                    butoncvp_5.timesOff[-1] = butoncvp_5.buttonClock.getTime() # update time clicked until
                if not butoncvp_5.wasClicked:
                    continueRoutine = False  # end routine when butoncvp_5 is clicked
                    None
                butoncvp_5.wasClicked = True  # if butoncvp_5 is still clicked next frame, it is not a new click
            else:
                butoncvp_5.wasClicked = False  # if butoncvp_5 is clicked next frame, it is a new click
        else:
            butoncvp_5.wasClicked = False  # if butoncvp_5 is clicked next frame, it is a new click
        
        # *noise_3* updates
        if noise_3.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            noise_3.frameNStart = frameN  # exact frame index
            noise_3.tStart = t  # local t and not account for scr refresh
            noise_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_3, 'tStartRefresh')  # time at next scr refresh
            noise_3.setAutoDraw(True)
        if noise_3.status == STARTED:
            if noise_3._needBuild:
                noise_3.buildNoise()
        
        # *süre_2* updates
        if süre_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            süre_2.frameNStart = frameN  # exact frame index
            süre_2.tStart = t  # local t and not account for scr refresh
            süre_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(süre_2, 'tStartRefresh')  # time at next scr refresh
            süre_2.setAutoDraw(True)
        if süre_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 25-frameTolerance:
                # keep track of stop time/frame for later
                süre_2.tStop = t  # not accounting for scr refresh
                süre_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(süre_2, 'tStopRefresh')  # time at next scr refresh
                süre_2.setAutoDraw(False)
        if süre_2.status == STARTED:  # only update if drawing
            süre_2.setText("Kalan süre: {0}".format(int(25-t)), log=False)
        
        # *timeuptext_2* updates
        if timeuptext_2.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            timeuptext_2.frameNStart = frameN  # exact frame index
            timeuptext_2.tStart = t  # local t and not account for scr refresh
            timeuptext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeuptext_2, 'tStartRefresh')  # time at next scr refresh
            timeuptext_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cattell2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cattell2_2"-------
    for thisComponent in cattell2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    cattell2.addData('butoncvp_1.started', butoncvp_1.tStartRefresh)
    cattell2.addData('butoncvp_1.stopped', butoncvp_1.tStopRefresh)
    cattell2.addData('butoncvp_1.numClicks', butoncvp_1.numClicks)
    if butoncvp_1.numClicks:
       cattell2.addData('butoncvp_1.timesOn', butoncvp_1.timesOn)
       cattell2.addData('butoncvp_1.timesOff', butoncvp_1.timesOff)
    else:
       cattell2.addData('butoncvp_1.timesOn', "")
       cattell2.addData('butoncvp_1.timesOff', "")
    cattell2.addData('butoncvp_2.started', butoncvp_2.tStartRefresh)
    cattell2.addData('butoncvp_2.stopped', butoncvp_2.tStopRefresh)
    cattell2.addData('butoncvp_2.numClicks', butoncvp_2.numClicks)
    if butoncvp_2.numClicks:
       cattell2.addData('butoncvp_2.timesOn', butoncvp_2.timesOn)
       cattell2.addData('butoncvp_2.timesOff', butoncvp_2.timesOff)
    else:
       cattell2.addData('butoncvp_2.timesOn', "")
       cattell2.addData('butoncvp_2.timesOff', "")
    cattell2.addData('butoncvp_3.started', butoncvp_3.tStartRefresh)
    cattell2.addData('butoncvp_3.stopped', butoncvp_3.tStopRefresh)
    cattell2.addData('butoncvp_3.numClicks', butoncvp_3.numClicks)
    if butoncvp_3.numClicks:
       cattell2.addData('butoncvp_3.timesOn', butoncvp_3.timesOn)
       cattell2.addData('butoncvp_3.timesOff', butoncvp_3.timesOff)
    else:
       cattell2.addData('butoncvp_3.timesOn', "")
       cattell2.addData('butoncvp_3.timesOff', "")
    cattell2.addData('butoncvp_4.started', butoncvp_4.tStartRefresh)
    cattell2.addData('butoncvp_4.stopped', butoncvp_4.tStopRefresh)
    cattell2.addData('butoncvp_4.numClicks', butoncvp_4.numClicks)
    if butoncvp_4.numClicks:
       cattell2.addData('butoncvp_4.timesOn', butoncvp_4.timesOn)
       cattell2.addData('butoncvp_4.timesOff', butoncvp_4.timesOff)
    else:
       cattell2.addData('butoncvp_4.timesOn', "")
       cattell2.addData('butoncvp_4.timesOff', "")
    cattell2.addData('butoncvp_5.started', butoncvp_5.tStartRefresh)
    cattell2.addData('butoncvp_5.stopped', butoncvp_5.tStopRefresh)
    cattell2.addData('butoncvp_5.numClicks', butoncvp_5.numClicks)
    if butoncvp_5.numClicks:
       cattell2.addData('butoncvp_5.timesOn', butoncvp_5.timesOn)
       cattell2.addData('butoncvp_5.timesOff', butoncvp_5.timesOff)
    else:
       cattell2.addData('butoncvp_5.timesOn', "")
       cattell2.addData('butoncvp_5.timesOff', "")
    # the Routine "cattell2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    soundd.setSound(correct, secs=1, hamming=True)
    soundd.setVolume(1.0, log=False)
    feedback_text.setText(correct_text)
    # keep track of which components have finished
    feedbackComponents = [soundd, feedback_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop soundd
        if soundd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            soundd.frameNStart = frameN  # exact frame index
            soundd.tStart = t  # local t and not account for scr refresh
            soundd.tStartRefresh = tThisFlipGlobal  # on global time
            soundd.play(when=win)  # sync with win flip
        if soundd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > soundd.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                soundd.tStop = t  # not accounting for scr refresh
                soundd.frameNStop = frameN  # exact frame index
                win.timeOnFlip(soundd, 'tStopRefresh')  # time at next scr refresh
                soundd.stop()
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    soundd.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'cattell2'

# get names of stimulus parameters
if cattell2.trialList in ([], [None], None):
    params = []
else:
    params = cattell2.trialList[0].keys()
# save data for this loop
cattell2.saveAsExcel(filename + '.xlsx', sheetName='cattell2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
cattell2.saveAsText(filename + 'cattell2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "toplampuan"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
toplampuanComponents = [toplam, tamam7_2, mouse_4]
for thisComponent in toplampuanComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
toplampuanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "toplampuan"-------
while continueRoutine:
    # get current time
    t = toplampuanClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=toplampuanClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *toplam* updates
    if toplam.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        toplam.frameNStart = frameN  # exact frame index
        toplam.tStart = t  # local t and not account for scr refresh
        toplam.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(toplam, 'tStartRefresh')  # time at next scr refresh
        toplam.setAutoDraw(True)
    
    # *tamam7_2* updates
    if tamam7_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamam7_2.frameNStart = frameN  # exact frame index
        tamam7_2.tStart = t  # local t and not account for scr refresh
        tamam7_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamam7_2, 'tStartRefresh')  # time at next scr refresh
        tamam7_2.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamam7_2)
                    clickableList = tamam7_2
                except:
                    clickableList = [tamam7_2]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in toplampuanComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "toplampuan"-------
for thisComponent in toplampuanComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tamam7_2.started', tamam7_2.tStartRefresh)
thisExp.addData('tamam7_2.stopped', tamam7_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamam7_2)
        clickableList = tamam7_2
    except:
        clickableList = [tamam7_2]
    for obj in clickableList:
        if obj.contains(mouse_4):
            gotValidClick = True
            mouse_4.clicked_name.append(obj.name)
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
if len(mouse_4.clicked_name):
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
# the Routine "toplampuan" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "session_end"-------
continueRoutine = True
# update component parameters for each repeat
telegram_send.send(messages=["Aşama sona erdi."])
# keep track of which components have finished
session_endComponents = []
for thisComponent in session_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
session_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "session_end"-------
while continueRoutine:
    # get current time
    t = session_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=session_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in session_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "session_end"-------
for thisComponent in session_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "session_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "testbilgi"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_9
mouse_9.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
testbilgiComponents = [colorblue_9, mouse_9, tamam7, sonasamabilgitxt]
for thisComponent in testbilgiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testbilgiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testbilgi"-------
while continueRoutine:
    # get current time
    t = testbilgiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testbilgiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_9* updates
    if colorblue_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_9.frameNStart = frameN  # exact frame index
        colorblue_9.tStart = t  # local t and not account for scr refresh
        colorblue_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_9, 'tStartRefresh')  # time at next scr refresh
        colorblue_9.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamam7)
                    clickableList = tamam7
                except:
                    clickableList = [tamam7]
                for obj in clickableList:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamam7* updates
    if tamam7.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamam7.frameNStart = frameN  # exact frame index
        tamam7.tStart = t  # local t and not account for scr refresh
        tamam7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamam7, 'tStartRefresh')  # time at next scr refresh
        tamam7.setAutoDraw(True)
    
    # *sonasamabilgitxt* updates
    if sonasamabilgitxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sonasamabilgitxt.frameNStart = frameN  # exact frame index
        sonasamabilgitxt.tStart = t  # local t and not account for scr refresh
        sonasamabilgitxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sonasamabilgitxt, 'tStartRefresh')  # time at next scr refresh
        sonasamabilgitxt.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testbilgiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testbilgi"-------
for thisComponent in testbilgiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_9.getPos()
buttons = mouse_9.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamam7)
        clickableList = tamam7
    except:
        clickableList = [tamam7]
    for obj in clickableList:
        if obj.contains(mouse_9):
            gotValidClick = True
            mouse_9.clicked_name.append(obj.name)
thisExp.addData('mouse_9.x', x)
thisExp.addData('mouse_9.y', y)
thisExp.addData('mouse_9.leftButton', buttons[0])
thisExp.addData('mouse_9.midButton', buttons[1])
thisExp.addData('mouse_9.rightButton', buttons[2])
if len(mouse_9.clicked_name):
    thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
thisExp.addData('mouse_9.started', mouse_9.tStart)
thisExp.addData('mouse_9.stopped', mouse_9.tStop)
thisExp.nextEntry()
thisExp.addData('tamam7.started', tamam7.tStartRefresh)
thisExp.addData('tamam7.stopped', tamam7.tStopRefresh)
thisExp.addData('sonasamabilgitxt.started', sonasamabilgitxt.tStartRefresh)
thisExp.addData('sonasamabilgitxt.stopped', sonasamabilgitxt.tStopRefresh)
# the Routine "testbilgi" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
duygu2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('duygusorular.xlsx'),
    seed=None, name='duygu2')
thisExp.addLoop(duygu2)  # add the loop to the experiment
thisDuygu2 = duygu2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDuygu2.rgb)
if thisDuygu2 != None:
    for paramName in thisDuygu2:
        exec('{} = thisDuygu2[paramName]'.format(paramName))

for thisDuygu2 in duygu2:
    currentLoop = duygu2
    # abbreviate parameter names if possible (e.g. rgb = thisDuygu2.rgb)
    if thisDuygu2 != None:
        for paramName in thisDuygu2:
            exec('{} = thisDuygu2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "duygular"-------
    continueRoutine = True
    # update component parameters for each repeat
    #yanda olması için exp değerleri: (0.55, -.095)
    thisPos = 0
    marker = slider.getMarkerPos()
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
        labels=("0", "10","20", "30", "40", "50", "60", "70", "80", "90", "100"), ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=5.0,
        style='rating', styleTweaks=(), opacity=1,
        color='black', fillColor='black', borderColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, depth=-1, readOnly=False)
    slider.marker = visual.Rect(
        win=win, name='polygon',units=None, 
        width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
        ori=0.0, pos=(0,-3),
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
        opacity=None, depth=-9.0, interpolate=True)
    slider.tickLines.opacities = 0
    slider.reset()
    # setup some python lists for storing info about the trialbitiren
    trialbitiren.clicked_name = []
    gotValidClick = False  # until a click is received
    bitti.setImage('tamam.png')
    negatiftext.setText(negatif)
    pozitiftext.setText(pozitif)
    notrtext.setText(notr)
    # keep track of which components have finished
    duygularComponents = [slider, ratingText, slidersoru, trialbitiren, bitti, negatiftext, pozitiftext, notrtext, fakemarker_2, arrows]
    for thisComponent in duygularComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    duygularClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "duygular"-------
    while continueRoutine:
        # get current time
        t = duygularClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=duygularClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if slider.getMarkerPos() != None:
            thisPos = (slider.getMarkerPos() / 100)-0.5
            marker = int(slider.getMarkerPos())
        else:
            marker = ""
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *ratingText* updates
        if ratingText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ratingText.frameNStart = frameN  # exact frame index
            ratingText.tStart = t  # local t and not account for scr refresh
            ratingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText, 'tStartRefresh')  # time at next scr refresh
            ratingText.setAutoDraw(True)
        if ratingText.status == STARTED:  # only update if drawing
            ratingText.setPos((thisPos, -0.035), log=False)
            ratingText.setText(str(marker), log=False)
        
        # *slidersoru* updates
        if slidersoru.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            slidersoru.frameNStart = frameN  # exact frame index
            slidersoru.tStart = t  # local t and not account for scr refresh
            slidersoru.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slidersoru, 'tStartRefresh')  # time at next scr refresh
            slidersoru.setAutoDraw(True)
        if slidersoru.status == STARTED:  # only update if drawing
            slidersoru.setPos((0, 0.2), log=False)
        # *trialbitiren* updates
        if trialbitiren.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            trialbitiren.frameNStart = frameN  # exact frame index
            trialbitiren.tStart = t  # local t and not account for scr refresh
            trialbitiren.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialbitiren, 'tStartRefresh')  # time at next scr refresh
            trialbitiren.status = STARTED
            trialbitiren.mouseClock.reset()
            prevButtonState = trialbitiren.getPressed()  # if button is down already this ISN'T a new click
        if trialbitiren.status == STARTED:  # only update if started and not finished!
            buttons = trialbitiren.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bitti)
                        clickableList = bitti
                    except:
                        clickableList = [bitti]
                    for obj in clickableList:
                        if obj.contains(trialbitiren):
                            gotValidClick = True
                            trialbitiren.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *bitti* updates
        if bitti.status == NOT_STARTED and marker is not "":
            # keep track of start time/frame for later
            bitti.frameNStart = frameN  # exact frame index
            bitti.tStart = t  # local t and not account for scr refresh
            bitti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitti, 'tStartRefresh')  # time at next scr refresh
            bitti.setAutoDraw(True)
        
        # *negatiftext* updates
        if negatiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            negatiftext.frameNStart = frameN  # exact frame index
            negatiftext.tStart = t  # local t and not account for scr refresh
            negatiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negatiftext, 'tStartRefresh')  # time at next scr refresh
            negatiftext.setAutoDraw(True)
        
        # *pozitiftext* updates
        if pozitiftext.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            pozitiftext.frameNStart = frameN  # exact frame index
            pozitiftext.tStart = t  # local t and not account for scr refresh
            pozitiftext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pozitiftext, 'tStartRefresh')  # time at next scr refresh
            pozitiftext.setAutoDraw(True)
        
        # *notrtext* updates
        if notrtext.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            notrtext.frameNStart = frameN  # exact frame index
            notrtext.tStart = t  # local t and not account for scr refresh
            notrtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notrtext, 'tStartRefresh')  # time at next scr refresh
            notrtext.setAutoDraw(True)
        
        # *fakemarker_2* updates
        if fakemarker_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            fakemarker_2.frameNStart = frameN  # exact frame index
            fakemarker_2.tStart = t  # local t and not account for scr refresh
            fakemarker_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fakemarker_2, 'tStartRefresh')  # time at next scr refresh
            fakemarker_2.setAutoDraw(True)
        if fakemarker_2.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                fakemarker_2.tStop = t  # not accounting for scr refresh
                fakemarker_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fakemarker_2, 'tStopRefresh')  # time at next scr refresh
                fakemarker_2.setAutoDraw(False)
        
        # *arrows* updates
        if arrows.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            arrows.frameNStart = frameN  # exact frame index
            arrows.tStart = t  # local t and not account for scr refresh
            arrows.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows, 'tStartRefresh')  # time at next scr refresh
            arrows.setAutoDraw(True)
        if arrows.status == STARTED:
            if bool(slider.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                arrows.tStop = t  # not accounting for scr refresh
                arrows.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrows, 'tStopRefresh')  # time at next scr refresh
                arrows.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in duygularComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "duygular"-------
    for thisComponent in duygularComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duygu2.addData('slider.response', slider.getRating())
    duygu2.addData('slider.rt', slider.getRT())
    # store data for duygu2 (TrialHandler)
    # the Routine "duygular" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'duygu2'

# get names of stimulus parameters
if duygu2.trialList in ([], [None], None):
    params = []
else:
    params = duygu2.trialList[0].keys()
# save data for this loop
duygu2.saveAsExcel(filename + '.xlsx', sheetName='duygu2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
duygu2.saveAsText(filename + 'duygu2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
hataloop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('hataruminasyon.xlsx'),
    seed=None, name='hataloop')
thisExp.addLoop(hataloop)  # add the loop to the experiment
thisHataloop = hataloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHataloop.rgb)
if thisHataloop != None:
    for paramName in thisHataloop:
        exec('{} = thisHataloop[paramName]'.format(paramName))

for thisHataloop in hataloop:
    currentLoop = hataloop
    # abbreviate parameter names if possible (e.g. rgb = thisHataloop.rgb)
    if thisHataloop != None:
        for paramName in thisHataloop:
            exec('{} = thisHataloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "hataruminasyon"-------
    continueRoutine = True
    # update component parameters for each repeat
    hataslider.reset()
    sorular_2.setText(itemText)
    # setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    hataruminasyonComponents = [hataslider, sorular_2, tamam8, mouse_10, hatarumklvztxt]
    for thisComponent in hataruminasyonComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    hataruminasyonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "hataruminasyon"-------
    while continueRoutine:
        # get current time
        t = hataruminasyonClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=hataruminasyonClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hataslider* updates
        if hataslider.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            hataslider.frameNStart = frameN  # exact frame index
            hataslider.tStart = t  # local t and not account for scr refresh
            hataslider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hataslider, 'tStartRefresh')  # time at next scr refresh
            hataslider.setAutoDraw(True)
        
        # *sorular_2* updates
        if sorular_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sorular_2.frameNStart = frameN  # exact frame index
            sorular_2.tStart = t  # local t and not account for scr refresh
            sorular_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sorular_2, 'tStartRefresh')  # time at next scr refresh
            sorular_2.setAutoDraw(True)
        
        # *tamam8* updates
        if tamam8.status == NOT_STARTED and hataslider.getMarkerPos() is not None:
            # keep track of start time/frame for later
            tamam8.frameNStart = frameN  # exact frame index
            tamam8.tStart = t  # local t and not account for scr refresh
            tamam8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tamam8, 'tStartRefresh')  # time at next scr refresh
            tamam8.setAutoDraw(True)
        # *mouse_10* updates
        if mouse_10.status == NOT_STARTED and hataslider.getMarkerPos() is not None:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(tamam8)
                        clickableList = tamam8
                    except:
                        clickableList = [tamam8]
                    for obj in clickableList:
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *hatarumklvztxt* updates
        if hatarumklvztxt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            hatarumklvztxt.frameNStart = frameN  # exact frame index
            hatarumklvztxt.tStart = t  # local t and not account for scr refresh
            hatarumklvztxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hatarumklvztxt, 'tStartRefresh')  # time at next scr refresh
            hatarumklvztxt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in hataruminasyonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "hataruminasyon"-------
    for thisComponent in hataruminasyonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    hataloop.addData('hataslider.response', hataslider.getRating())
    hataloop.addData('hataslider.rt', hataslider.getRT())
    # store data for hataloop (TrialHandler)
    hataloop.addData('hatarumklvztxt.started', hatarumklvztxt.tStartRefresh)
    hataloop.addData('hatarumklvztxt.stopped', hatarumklvztxt.tStopRefresh)
    # the Routine "hataruminasyon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'hataloop'

# get names of stimulus parameters
if hataloop.trialList in ([], [None], None):
    params = []
else:
    params = hataloop.trialList[0].keys()
# save data for this loop
hataloop.saveAsExcel(filename + '.xlsx', sheetName='hataloop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
hataloop.saveAsText(filename + 'hataloop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
brsi2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bsri.xlsx'),
    seed=None, name='brsi2')
thisExp.addLoop(brsi2)  # add the loop to the experiment
thisBrsi2 = brsi2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBrsi2.rgb)
if thisBrsi2 != None:
    for paramName in thisBrsi2:
        exec('{} = thisBrsi2[paramName]'.format(paramName))

for thisBrsi2 in brsi2:
    currentLoop = brsi2
    # abbreviate parameter names if possible (e.g. rgb = thisBrsi2.rgb)
    if thisBrsi2 != None:
        for paramName in thisBrsi2:
            exec('{} = thisBrsi2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ruminasyon"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_2.reset()
    ruminasyonsorular.setText(itemText)
    # setup some python lists for storing info about the trialbitiren_2
    trialbitiren_2.clicked_name = []
    gotValidClick = False  # until a click is received
    thisPoss = 0
    markerr = ""
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.1), units=None,
        labels=("0", "10","20", "30", "40", "50", "60", "70", "80", "90", "100"), ticks=[0,10,20,30,40,50,60,70,80,90,100], granularity=5.0,
        style='rating', styleTweaks=(), opacity=1,
        color='black', fillColor='black', borderColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, depth=-1, readOnly=False)
    slider_2.marker = visual.Rect(
        win=win, name='polygon',units=None, 
        width=(0.01, 0.1)[0], height=(0.01, 0.1)[1],
        ori=0.0, pos=(0,-3),
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -0.0588, 0.6863], fillColor=[-1.0000, -0.0588, 0.6863],
        opacity=None, depth=-9.0, interpolate=True)
    slider_2.tickLines.opacities = 0
    # keep track of which components have finished
    ruminasyonComponents = [slider_2, ruminasyonsorular, bitti_2, trialbitiren_2, ratingText_2, ruminasyonklvz, fakemarker_3, negatiftext_2, pozitiftext_2, arrows_2]
    for thisComponent in ruminasyonComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ruminasyonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ruminasyon"-------
    while continueRoutine:
        # get current time
        t = ruminasyonClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ruminasyonClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        
        # *ruminasyonsorular* updates
        if ruminasyonsorular.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ruminasyonsorular.frameNStart = frameN  # exact frame index
            ruminasyonsorular.tStart = t  # local t and not account for scr refresh
            ruminasyonsorular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ruminasyonsorular, 'tStartRefresh')  # time at next scr refresh
            ruminasyonsorular.setAutoDraw(True)
        
        # *bitti_2* updates
        if bitti_2.status == NOT_STARTED and markerr is not "":
            # keep track of start time/frame for later
            bitti_2.frameNStart = frameN  # exact frame index
            bitti_2.tStart = t  # local t and not account for scr refresh
            bitti_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitti_2, 'tStartRefresh')  # time at next scr refresh
            bitti_2.setAutoDraw(True)
        # *trialbitiren_2* updates
        if trialbitiren_2.status == NOT_STARTED and markerr is not "":
            # keep track of start time/frame for later
            trialbitiren_2.frameNStart = frameN  # exact frame index
            trialbitiren_2.tStart = t  # local t and not account for scr refresh
            trialbitiren_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialbitiren_2, 'tStartRefresh')  # time at next scr refresh
            trialbitiren_2.status = STARTED
            trialbitiren_2.mouseClock.reset()
            prevButtonState = trialbitiren_2.getPressed()  # if button is down already this ISN'T a new click
        if trialbitiren_2.status == STARTED:  # only update if started and not finished!
            buttons = trialbitiren_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bitti_2)
                        clickableList = bitti_2
                    except:
                        clickableList = [bitti_2]
                    for obj in clickableList:
                        if obj.contains(trialbitiren_2):
                            gotValidClick = True
                            trialbitiren_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        if slider_2.getMarkerPos() is None:
            thisPoss = 0
            markerr = ""
        else:
            thisPoss = (slider_2.getMarkerPos() / 100)-0.5
            markerr = int(slider_2.getMarkerPos())
        
        # *ratingText_2* updates
        if ratingText_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ratingText_2.frameNStart = frameN  # exact frame index
            ratingText_2.tStart = t  # local t and not account for scr refresh
            ratingText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText_2, 'tStartRefresh')  # time at next scr refresh
            ratingText_2.setAutoDraw(True)
        if ratingText_2.status == STARTED:  # only update if drawing
            ratingText_2.setPos((thisPoss, -.025), log=False)
            ratingText_2.setText(str(markerr), log=False)
        
        # *ruminasyonklvz* updates
        if ruminasyonklvz.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ruminasyonklvz.frameNStart = frameN  # exact frame index
            ruminasyonklvz.tStart = t  # local t and not account for scr refresh
            ruminasyonklvz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ruminasyonklvz, 'tStartRefresh')  # time at next scr refresh
            ruminasyonklvz.setAutoDraw(True)
        
        # *fakemarker_3* updates
        if fakemarker_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            fakemarker_3.frameNStart = frameN  # exact frame index
            fakemarker_3.tStart = t  # local t and not account for scr refresh
            fakemarker_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fakemarker_3, 'tStartRefresh')  # time at next scr refresh
            fakemarker_3.setAutoDraw(True)
        if fakemarker_3.status == STARTED:
            if bool(slider_2.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                fakemarker_3.tStop = t  # not accounting for scr refresh
                fakemarker_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fakemarker_3, 'tStopRefresh')  # time at next scr refresh
                fakemarker_3.setAutoDraw(False)
        
        # *negatiftext_2* updates
        if negatiftext_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            negatiftext_2.frameNStart = frameN  # exact frame index
            negatiftext_2.tStart = t  # local t and not account for scr refresh
            negatiftext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negatiftext_2, 'tStartRefresh')  # time at next scr refresh
            negatiftext_2.setAutoDraw(True)
        
        # *pozitiftext_2* updates
        if pozitiftext_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            pozitiftext_2.frameNStart = frameN  # exact frame index
            pozitiftext_2.tStart = t  # local t and not account for scr refresh
            pozitiftext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pozitiftext_2, 'tStartRefresh')  # time at next scr refresh
            pozitiftext_2.setAutoDraw(True)
        
        # *arrows_2* updates
        if arrows_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            arrows_2.frameNStart = frameN  # exact frame index
            arrows_2.tStart = t  # local t and not account for scr refresh
            arrows_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows_2, 'tStartRefresh')  # time at next scr refresh
            arrows_2.setAutoDraw(True)
        if arrows_2.status == STARTED:
            if bool(slider_2.getMarkerPos() is not None):
                # keep track of stop time/frame for later
                arrows_2.tStop = t  # not accounting for scr refresh
                arrows_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrows_2, 'tStopRefresh')  # time at next scr refresh
                arrows_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ruminasyonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ruminasyon"-------
    for thisComponent in ruminasyonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    brsi2.addData('slider_2.response', slider_2.getRating())
    brsi2.addData('slider_2.rt', slider_2.getRT())
    # store data for brsi2 (TrialHandler)
    # the Routine "ruminasyon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'brsi2'

# get names of stimulus parameters
if brsi2.trialList in ([], [None], None):
    params = []
else:
    params = brsi2.trialList[0].keys()
# save data for this loop
brsi2.saveAsExcel(filename + '.xlsx', sheetName='brsi2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
brsi2.saveAsText(filename + 'brsi2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "navonbilgi2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_8
mouse_8.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
navonbilgi2Components = [colorblue_10, mouse_8, tamam6, text_4, orneknavonimg_2]
for thisComponent in navonbilgi2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
navonbilgi2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "navonbilgi2"-------
while continueRoutine:
    # get current time
    t = navonbilgi2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=navonbilgi2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_10* updates
    if colorblue_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_10.frameNStart = frameN  # exact frame index
        colorblue_10.tStart = t  # local t and not account for scr refresh
        colorblue_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_10, 'tStartRefresh')  # time at next scr refresh
        colorblue_10.setAutoDraw(True)
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(tamam6)
                    clickableList = tamam6
                except:
                    clickableList = [tamam6]
                for obj in clickableList:
                    if obj.contains(mouse_8):
                        gotValidClick = True
                        mouse_8.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *tamam6* updates
    if tamam6.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        tamam6.frameNStart = frameN  # exact frame index
        tamam6.tStart = t  # local t and not account for scr refresh
        tamam6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tamam6, 'tStartRefresh')  # time at next scr refresh
        tamam6.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *orneknavonimg_2* updates
    if orneknavonimg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        orneknavonimg_2.frameNStart = frameN  # exact frame index
        orneknavonimg_2.tStart = t  # local t and not account for scr refresh
        orneknavonimg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(orneknavonimg_2, 'tStartRefresh')  # time at next scr refresh
        orneknavonimg_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in navonbilgi2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "navonbilgi2"-------
for thisComponent in navonbilgi2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_8.getPos()
buttons = mouse_8.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(tamam6)
        clickableList = tamam6
    except:
        clickableList = [tamam6]
    for obj in clickableList:
        if obj.contains(mouse_8):
            gotValidClick = True
            mouse_8.clicked_name.append(obj.name)
thisExp.addData('mouse_8.x', x)
thisExp.addData('mouse_8.y', y)
thisExp.addData('mouse_8.leftButton', buttons[0])
thisExp.addData('mouse_8.midButton', buttons[1])
thisExp.addData('mouse_8.rightButton', buttons[2])
if len(mouse_8.clicked_name):
    thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
thisExp.addData('mouse_8.started', mouse_8.tStart)
thisExp.addData('mouse_8.stopped', mouse_8.tStop)
thisExp.nextEntry()
thisExp.addData('tamam6.started', tamam6.tStartRefresh)
thisExp.addData('tamam6.stopped', tamam6.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "navonbilgi2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(9.900000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [colorblue_8, text_2, text_5]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_8* updates
    if colorblue_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_8.frameNStart = frameN  # exact frame index
        colorblue_8.tStart = t  # local t and not account for scr refresh
        colorblue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_8, 'tStartRefresh')  # time at next scr refresh
        colorblue_8.setAutoDraw(True)
    if colorblue_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > colorblue_8.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            colorblue_8.tStop = t  # not accounting for scr refresh
            colorblue_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(colorblue_8, 'tStopRefresh')  # time at next scr refresh
            colorblue_8.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    if text_5.status == STARTED:  # only update if drawing
        text_5.setText(str(round((10-t),1)), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
navonblok3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('navon.xlsx', selection='0:20'),
    seed=None, name='navonblok3')
thisExp.addLoop(navonblok3)  # add the loop to the experiment
thisNavonblok3 = navonblok3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNavonblok3.rgb)
if thisNavonblok3 != None:
    for paramName in thisNavonblok3:
        exec('{} = thisNavonblok3[paramName]'.format(paramName))

for thisNavonblok3 in navonblok3:
    currentLoop = navonblok3
    # abbreviate parameter names if possible (e.g. rgb = thisNavonblok3.rgb)
    if thisNavonblok3 != None:
        for paramName in thisNavonblok3:
            exec('{} = thisNavonblok3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "navon_3"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    letter_4.setPos((navonpose, 0))
    letter_4.setImage(soru)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    noise_6.setPos((navonpose, 0))
    # keep track of which components have finished
    navon_3Components = [letter_4, fix_4, key_resp_6, noise_6]
    for thisComponent in navon_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    navon_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "navon_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = navon_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=navon_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letter_4* updates
        if letter_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            letter_4.frameNStart = frameN  # exact frame index
            letter_4.tStart = t  # local t and not account for scr refresh
            letter_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter_4, 'tStartRefresh')  # time at next scr refresh
            letter_4.setAutoDraw(True)
        if letter_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter_4.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                letter_4.tStop = t  # not accounting for scr refresh
                letter_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter_4, 'tStopRefresh')  # time at next scr refresh
                letter_4.setAutoDraw(False)
        
        # *fix_4* updates
        if fix_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_4.frameNStart = frameN  # exact frame index
            fix_4.tStart = t  # local t and not account for scr refresh
            fix_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_4, 'tStartRefresh')  # time at next scr refresh
            fix_4.setAutoDraw(True)
        if fix_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_4.tStop = t  # not accounting for scr refresh
                fix_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_4, 'tStopRefresh')  # time at next scr refresh
                fix_4.setAutoDraw(False)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_6.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_6.tStop = t  # not accounting for scr refresh
                key_resp_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
                key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noise_6* updates
        if noise_6.status == NOT_STARTED and tThisFlip >= 0.65-frameTolerance:
            # keep track of start time/frame for later
            noise_6.frameNStart = frameN  # exact frame index
            noise_6.tStart = t  # local t and not account for scr refresh
            noise_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_6, 'tStartRefresh')  # time at next scr refresh
            noise_6.setAutoDraw(True)
        if noise_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_6.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                noise_6.tStop = t  # not accounting for scr refresh
                noise_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_6, 'tStopRefresh')  # time at next scr refresh
                noise_6.setAutoDraw(False)
        if noise_6.status == STARTED:
            if noise_6._needBuild:
                noise_6.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in navon_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "navon_3"-------
    for thisComponent in navon_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    navonblok3.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        navonblok3.addData('key_resp_6.rt', key_resp_6.rt)
    if key_resp_6.keys==correctAns:
        navonblok3.addData('correct',1);
    elif correctAns==None:
        navonblok3.addData('correct',1);
    else:
        navonblok3.addData('correct',0)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'navonblok3'

# get names of stimulus parameters
if navonblok3.trialList in ([], [None], None):
    params = []
else:
    params = navonblok3.trialList[0].keys()
# save data for this loop
navonblok3.saveAsExcel(filename + '.xlsx', sheetName='navonblok3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
navonblok3.saveAsText(filename + 'navonblok3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "interval"-------
continueRoutine = True
routineTimer.add(59.900000)
# update component parameters for each repeat
line_lenght = 30
# keep track of which components have finished
intervalComponents = [countdown, timer_line, mola]
for thisComponent in intervalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "interval"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intervalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intervalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *countdown* updates
    if countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        countdown.frameNStart = frameN  # exact frame index
        countdown.tStart = t  # local t and not account for scr refresh
        countdown.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown, 'tStartRefresh')  # time at next scr refresh
        countdown.setAutoDraw(True)
    if countdown.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            countdown.tStop = t  # not accounting for scr refresh
            countdown.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown, 'tStopRefresh')  # time at next scr refresh
            countdown.setAutoDraw(False)
    if countdown.status == STARTED:  # only update if drawing
        countdown.setText(round(60-t, ndigits=1), log=False)
    line_lenght = (30-(t/2))
    
    # *timer_line* updates
    if timer_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        timer_line.frameNStart = frameN  # exact frame index
        timer_line.tStart = t  # local t and not account for scr refresh
        timer_line.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(timer_line, 'tStartRefresh')  # time at next scr refresh
        timer_line.setAutoDraw(True)
    if timer_line.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > timer_line.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            timer_line.tStop = t  # not accounting for scr refresh
            timer_line.frameNStop = frameN  # exact frame index
            win.timeOnFlip(timer_line, 'tStopRefresh')  # time at next scr refresh
            timer_line.setAutoDraw(False)
    if timer_line.status == STARTED:  # only update if drawing
        timer_line.setSize((line_lenght, 1), log=False)
    
    # *mola* updates
    if mola.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mola.frameNStart = frameN  # exact frame index
        mola.tStart = t  # local t and not account for scr refresh
        mola.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mola, 'tStartRefresh')  # time at next scr refresh
        mola.setAutoDraw(True)
    if mola.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mola.tStartRefresh + 59.9-frameTolerance:
            # keep track of stop time/frame for later
            mola.tStop = t  # not accounting for scr refresh
            mola.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mola, 'tStopRefresh')  # time at next scr refresh
            mola.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "interval"-------
for thisComponent in intervalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mola.started', mola.tStartRefresh)
thisExp.addData('mola.stopped', mola.tStopRefresh)

# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(9.900000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [colorblue_8, text_2, text_5]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *colorblue_8* updates
    if colorblue_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        colorblue_8.frameNStart = frameN  # exact frame index
        colorblue_8.tStart = t  # local t and not account for scr refresh
        colorblue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(colorblue_8, 'tStartRefresh')  # time at next scr refresh
        colorblue_8.setAutoDraw(True)
    if colorblue_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > colorblue_8.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            colorblue_8.tStop = t  # not accounting for scr refresh
            colorblue_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(colorblue_8, 'tStopRefresh')  # time at next scr refresh
            colorblue_8.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 9.9-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    if text_5.status == STARTED:  # only update if drawing
        text_5.setText(str(round((10-t),1)), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
navonblok4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('navon.xlsx', selection='0:20'),
    seed=None, name='navonblok4')
thisExp.addLoop(navonblok4)  # add the loop to the experiment
thisNavonblok4 = navonblok4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNavonblok4.rgb)
if thisNavonblok4 != None:
    for paramName in thisNavonblok4:
        exec('{} = thisNavonblok4[paramName]'.format(paramName))

for thisNavonblok4 in navonblok4:
    currentLoop = navonblok4
    # abbreviate parameter names if possible (e.g. rgb = thisNavonblok4.rgb)
    if thisNavonblok4 != None:
        for paramName in thisNavonblok4:
            exec('{} = thisNavonblok4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "navon_4"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    letter_5.setPos((navonpose, 0))
    letter_5.setImage(soru)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    noise_7.setPos((navonpose, 0))
    # keep track of which components have finished
    navon_4Components = [letter_5, fix_5, key_resp_7, noise_7]
    for thisComponent in navon_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    navon_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "navon_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = navon_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=navon_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letter_5* updates
        if letter_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            letter_5.frameNStart = frameN  # exact frame index
            letter_5.tStart = t  # local t and not account for scr refresh
            letter_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter_5, 'tStartRefresh')  # time at next scr refresh
            letter_5.setAutoDraw(True)
        if letter_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter_5.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                letter_5.tStop = t  # not accounting for scr refresh
                letter_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter_5, 'tStopRefresh')  # time at next scr refresh
                letter_5.setAutoDraw(False)
        
        # *fix_5* updates
        if fix_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_5.frameNStart = frameN  # exact frame index
            fix_5.tStart = t  # local t and not account for scr refresh
            fix_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_5, 'tStartRefresh')  # time at next scr refresh
            fix_5.setAutoDraw(True)
        if fix_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_5.tStop = t  # not accounting for scr refresh
                fix_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_5, 'tStopRefresh')  # time at next scr refresh
                fix_5.setAutoDraw(False)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_7.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noise_7* updates
        if noise_7.status == NOT_STARTED and tThisFlip >= 0.65-frameTolerance:
            # keep track of start time/frame for later
            noise_7.frameNStart = frameN  # exact frame index
            noise_7.tStart = t  # local t and not account for scr refresh
            noise_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_7, 'tStartRefresh')  # time at next scr refresh
            noise_7.setAutoDraw(True)
        if noise_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_7.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                noise_7.tStop = t  # not accounting for scr refresh
                noise_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_7, 'tStopRefresh')  # time at next scr refresh
                noise_7.setAutoDraw(False)
        if noise_7.status == STARTED:
            if noise_7._needBuild:
                noise_7.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in navon_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "navon_4"-------
    for thisComponent in navon_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    navonblok4.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        navonblok4.addData('key_resp_7.rt', key_resp_7.rt)
    if key_resp_7.keys==correctAns:
        navonblok4.addData('correct',1);
    elif correctAns==None:
        navonblok4.addData('correct',1);
    else:
        navonblok4.addData('correct',0)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'navonblok4'

# get names of stimulus parameters
if navonblok4.trialList in ([], [None], None):
    params = []
else:
    params = navonblok4.trialList[0].keys()
# save data for this loop
navonblok4.saveAsExcel(filename + '.xlsx', sheetName='navonblok4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
navonblok4.saveAsText(filename + 'navonblok4.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "session_end"-------
continueRoutine = True
# update component parameters for each repeat
telegram_send.send(messages=["Aşama sona erdi."])
# keep track of which components have finished
session_endComponents = []
for thisComponent in session_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
session_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "session_end"-------
while continueRoutine:
    # get current time
    t = session_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=session_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in session_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "session_end"-------
for thisComponent in session_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "session_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
toplamlar = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='toplamlar')
thisExp.addLoop(toplamlar)  # add the loop to the experiment
thisToplamlar = toplamlar.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisToplamlar.rgb)
if thisToplamlar != None:
    for paramName in thisToplamlar:
        exec('{} = thisToplamlar[paramName]'.format(paramName))

for thisToplamlar in toplamlar:
    currentLoop = toplamlar
    # abbreviate parameter names if possible (e.g. rgb = thisToplamlar.rgb)
    if thisToplamlar != None:
        for paramName in thisToplamlar:
            exec('{} = thisToplamlar[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "expfin"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    expfinComponents = [colorblue_11, mouse_3, tamamm, finishingtxt]
    for thisComponent in expfinComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    expfinClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "expfin"-------
    while continueRoutine:
        # get current time
        t = expfinClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=expfinClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colorblue_11* updates
        if colorblue_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            colorblue_11.frameNStart = frameN  # exact frame index
            colorblue_11.tStart = t  # local t and not account for scr refresh
            colorblue_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colorblue_11, 'tStartRefresh')  # time at next scr refresh
            colorblue_11.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 5-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(tamamm)
                        clickableList = tamamm
                    except:
                        clickableList = [tamamm]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *tamamm* updates
        if tamamm.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            tamamm.frameNStart = frameN  # exact frame index
            tamamm.tStart = t  # local t and not account for scr refresh
            tamamm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tamamm, 'tStartRefresh')  # time at next scr refresh
            tamamm.setAutoDraw(True)
        
        # *finishingtxt* updates
        if finishingtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finishingtxt.frameNStart = frameN  # exact frame index
            finishingtxt.tStart = t  # local t and not account for scr refresh
            finishingtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finishingtxt, 'tStartRefresh')  # time at next scr refresh
            finishingtxt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expfinComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "expfin"-------
    for thisComponent in expfinComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for toplamlar (TrialHandler)
    navonblok1correct = navonblok1.data["correct"]
    navonblok2correct = navonblok2.data["correct"]
    navonblok3correct = navonblok3.data["correct"]
    navonblok4correct = navonblok4.data["correct"]
    duygufarksad = subtract(duygu1.data["slider.response"][0], duygu2.data["slider.response"][0])
    toplamlar.addData("duygu fark", duygufark)
    
    toplamnvn1 = "Navon İlk Test Toplam Puan: %i/160" %(navonblok1correct.sum()+navonblok2correct.sum())
    toplamnvn2 = "Navon Son Test Toplam Puan: %i/160" %(navonblok3correct.sum()+navonblok4correct.sum())
    
    
    toplamlar.addData("Navon Doğru Yüzdesi Ön Test", navonblok1correct.sum()+navonblok2correct.sum()/160)
    toplamlar.addData("Navon Doğru Yüzdesi Son Test", navonblok3correct.sum()+navonblok4correct.sum()/160)
    # the Routine "expfin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'toplamlar'

# get names of stimulus parameters
if toplamlar.trialList in ([], [None], None):
    params = []
else:
    params = toplamlar.trialList[0].keys()
# save data for this loop
toplamlar.saveAsExcel(filename + '.xlsx', sheetName='toplamlar',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
toplamlar.saveAsText(filename + 'toplamlar.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finnishhhhhh"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
finnishhhhhhComponents = [key_resp_4, text_6]
for thisComponent in finnishhhhhhComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finnishhhhhhClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finnishhhhhh"-------
while continueRoutine:
    # get current time
    t = finnishhhhhhClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finnishhhhhhClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['h'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finnishhhhhhComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finnishhhhhh"-------
for thisComponent in finnishhhhhhComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "finnishhhhhh" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='tab')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
