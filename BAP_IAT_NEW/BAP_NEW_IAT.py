#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on February 05, 2024, at 15:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from counterbalance
import math as Math 
import random
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'BAP_NEW_IAT'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\PychComp\\Desktop\\BAP_IAT_NEW\\BAP_NEW_IAT.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "countb" ---
    # Run 'Begin Experiment' code from counterbalance
    randNum = random.randint(0,1)
    
    if randNum == 0 :
        nRepsA=1
        nRepsB=0
        
    else:
        nRepsA=0
        nRepsB=1
    
    
    
    # --- Initialize components for Routine "general_instruction" ---
    text_generalinst = visual.TextStim(win=win, name='text_generalinst',
        text='Welcome to IAT!\n\nAşağıda 4 grup ve her gruba ait öğeler vardır: \n\nİyi : Şahane, Güzel, Sevimli, Mutlu, Hoş, Sevgi, Zafer, Memnun\n\nKötü : Hata, Felaket, Izdırap, Yaramaz, Korkunç, İğrenç, Şeytani, Çirkin\n\nBaşı örtülü Yüzler: Başı örtülü yüzler göreceksiniz - Örtülü\n\nBaşı örtülü olmayan Yüzler :Başı örtülü olmayan yüzler göreceksiniz- Örtüsüz\n\nDevam etmek için boşluk tuşuna basın ! ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok1_instruction1" ---
    text_blok1_instruction1 = visual.TextStim(win=win, name='text_blok1_instruction1',
        text='Başı örtüsüz yüzler için E kullanılacak. \n\nBaşı örütülü yüzler için I kullanılacak.\n\nEğer cevabınız yanlış ise siyah "X" işaretiyle karşılacaksınız. Doğru yapıtığınız zaman bir sonraki denemeye geçeceksiniz ! \n\n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_intr1 = keyboard.Keyboard()
    text_uncovered0 = visual.TextStim(win=win, name='text_uncovered0',
        text='Örtüsüz',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_Covered0 = visual.TextStim(win=win, name='text_Covered0',
        text='Örtülü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Blok_1_Main" ---
    target_image_blok1 = visual.ImageStim(
        win=win,
        name='target_image_blok1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok1_main = keyboard.Keyboard()
    text_uncovered_main = visual.TextStim(win=win, name='text_uncovered_main',
        text='Örtüsüz',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_covered_main = visual.TextStim(win=win, name='text_covered_main',
        text='Örtülü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok_1_feedback" ---
    text_fdb = visual.TextStim(win=win, name='text_fdb',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "rep_blok1" ---
    image_blok1_rep = visual.ImageStim(
        win=win,
        name='image_blok1_rep', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok1_rep = keyboard.Keyboard()
    text_rep_uncovered = visual.TextStim(win=win, name='text_rep_uncovered',
        text='Örtüsüz',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_rep_covered = visual.TextStim(win=win, name='text_rep_covered',
        text='Örtülü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok_1_1_feedback" ---
    text_rep_feed = visual.TextStim(win=win, name='text_rep_feed',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok2_instruction" ---
    text_blok2_inst = visual.TextStim(win=win, name='text_blok2_inst',
        text='\nEğer ekranda beliren sıfat\n\nİyi kategorisindeyse  - E\n\nkötü kategorisindeyse - I\n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok2_inst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Blok_2_Main" ---
    image_block2_main = visual.ImageStim(
        win=win,
        name='image_block2_main', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok2_main = keyboard.Keyboard()
    text_attractive_main = visual.TextStim(win=win, name='text_attractive_main',
        text='İyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_unattractive_main = visual.TextStim(win=win, name='text_unattractive_main',
        text='Kötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok_2_feedback" ---
    text_fdb_2 = visual.TextStim(win=win, name='text_fdb_2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "rep_blok2" ---
    image_block2_rep = visual.ImageStim(
        win=win,
        name='image_block2_rep', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok2_rep = keyboard.Keyboard()
    text_attractive_rep = visual.TextStim(win=win, name='text_attractive_rep',
        text='İyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_unattractive_rep = visual.TextStim(win=win, name='text_unattractive_rep',
        text='Kötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok_2_1_feedback" ---
    text_rep_feed_2 = visual.TextStim(win=win, name='text_rep_feed_2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok_3_instruction" ---
    text_blok3_ins = visual.TextStim(win=win, name='text_blok3_ins',
        text='\nEkranda beliren uyaran, \n\nÖrtüsüz yada İyi ise - E \n\nÖrtülü yada Kötü - I\n\nBaşlamak için boşluk tuşuna basın ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok3_inst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok_3_main1" ---
    target_image_blok3 = visual.ImageStim(
        win=win,
        name='target_image_blok3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok3_main_1 = keyboard.Keyboard()
    text_uncoveredattr_main = visual.TextStim(win=win, name='text_uncoveredattr_main',
        text='Örtüsüz\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_coveredunattr_main = visual.TextStim(win=win, name='text_coveredunattr_main',
        text='Örtülü\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok3_main1_feedback" ---
    text_fdb_3 = visual.TextStim(win=win, name='text_fdb_3',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok3_main1_rep" ---
    image_blok3_main1_rep = visual.ImageStim(
        win=win,
        name='image_blok3_main1_rep', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok3_main1_rep = keyboard.Keyboard()
    text_uncoveredattr_main_rep = visual.TextStim(win=win, name='text_uncoveredattr_main_rep',
        text='Örtüsüz\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_coveredunattr_main_rep = visual.TextStim(win=win, name='text_coveredunattr_main_rep',
        text='Örtülü\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok3_main1_rep_feedback" ---
    text_rep_feed_3 = visual.TextStim(win=win, name='text_rep_feed_3',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok_4_inst" ---
    text_blok4_ins = visual.TextStim(win=win, name='text_blok4_ins',
        text='Dikkat !\n\nEğer ekrana çıkan yüzlerin, \n\nBaşı örtülüyse -  E  \n\nBaşı örtüsüzse  - I  \n\n\nBaşlamak için boşluk tuşuna basın\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok4_inst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok4_main" ---
    target_image_blok4 = visual.ImageStim(
        win=win,
        name='target_image_blok4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok4_main = keyboard.Keyboard()
    text_covered_main_4 = visual.TextStim(win=win, name='text_covered_main_4',
        text='Örtülü',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncovered_main_4 = visual.TextStim(win=win, name='text_uncovered_main_4',
        text='Örtüsüz',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok4_main_feedback" ---
    text_fdb_5 = visual.TextStim(win=win, name='text_fdb_5',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok4_rep" ---
    target_image_blok4_rep = visual.ImageStim(
        win=win,
        name='target_image_blok4_rep', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok4_rep = keyboard.Keyboard()
    text_covered_rep_4 = visual.TextStim(win=win, name='text_covered_rep_4',
        text='Örtülü',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncovered_rep_4 = visual.TextStim(win=win, name='text_uncovered_rep_4',
        text='Örtüsüz',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok4_rep_feedback" ---
    text_rep_feed_4 = visual.TextStim(win=win, name='text_rep_feed_4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok_5_inst" ---
    text_blok5_ins = visual.TextStim(win=win, name='text_blok5_ins',
        text='\nEkrana çıkana uyaran,\n\nÖrtülü  yada  İyi ise -  E\n\nÖrtüsüz yada Kötü ise - I \n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok5_inst = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok5_main" ---
    target_image_blok5 = visual.ImageStim(
        win=win,
        name='target_image_blok5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok5_main = keyboard.Keyboard()
    text_coveredattr_main_5 = visual.TextStim(win=win, name='text_coveredattr_main_5',
        text='Örtülü\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncoveredunattr_main_5 = visual.TextStim(win=win, name='text_uncoveredunattr_main_5',
        text='Örtüsüz\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok5_main_feedback" ---
    text_fdb_6 = visual.TextStim(win=win, name='text_fdb_6',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok5_rep" ---
    target_image_blok5_rep = visual.ImageStim(
        win=win,
        name='target_image_blok5_rep', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok5_rep = keyboard.Keyboard()
    text_coveredattr_rep = visual.TextStim(win=win, name='text_coveredattr_rep',
        text='Örtülü\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncoveredunattr_rep = visual.TextStim(win=win, name='text_uncoveredunattr_rep',
        text='Örtüsüz\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok5_rep_feedback" ---
    text_rep_feed_5 = visual.TextStim(win=win, name='text_rep_feed_5',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "thanks_1" ---
    text_thanks1 = visual.TextStim(win=win, name='text_thanks1',
        text='thanks for participants',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_thanks1 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "exitcode1" ---
    
    # --- Initialize components for Routine "blok4_2ins" ---
    text_blok4_ins_2 = visual.TextStim(win=win, name='text_blok4_ins_2',
        text='Eğer ekrana çıkan yüzlerin, \n\nBaşı örtülüyse -  E  \n\nBaşı örtüsüzse  - I  \n\n\nBaşlamak için boşluk tuşuna basın\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok4_inst_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok4_main_2" ---
    target_image_blok4_2 = visual.ImageStim(
        win=win,
        name='target_image_blok4_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok4_main_2 = keyboard.Keyboard()
    text_covered_main_4_2 = visual.TextStim(win=win, name='text_covered_main_4_2',
        text='Örtülü',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncovered_main_4_2 = visual.TextStim(win=win, name='text_uncovered_main_4_2',
        text='Örtüsüz',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok4_main_2_feedback" ---
    text_fdb_7 = visual.TextStim(win=win, name='text_fdb_7',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok4_2_rep" ---
    target_image_blok4_rep_2 = visual.ImageStim(
        win=win,
        name='target_image_blok4_rep_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok4_rep_2 = keyboard.Keyboard()
    text_covered_rep_2 = visual.TextStim(win=win, name='text_covered_rep_2',
        text='Örtülü',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncovered_rep_2 = visual.TextStim(win=win, name='text_uncovered_rep_2',
        text='Örtüsüz',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok4_2_rep_feedback" ---
    text_rep_feed_4_2 = visual.TextStim(win=win, name='text_rep_feed_4_2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok2_2intr" ---
    text_blok2_inst_2 = visual.TextStim(win=win, name='text_blok2_inst_2',
        text='\nEğer ekranda beliren sıfat\n\nİyi kategorisindeyse  - E\n\nkötü kategorisindeyse - I\n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok2_inst_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok2_2_main" ---
    image_block2_main_2 = visual.ImageStim(
        win=win,
        name='image_block2_main_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok2_main_2 = keyboard.Keyboard()
    text_attractive_main_2 = visual.TextStim(win=win, name='text_attractive_main_2',
        text='İyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_unattractive_main_2 = visual.TextStim(win=win, name='text_unattractive_main_2',
        text='Kötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok2_2_main_feedback" ---
    text_fdb_8 = visual.TextStim(win=win, name='text_fdb_8',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok2_2_rep" ---
    image_block2_rep_2 = visual.ImageStim(
        win=win,
        name='image_block2_rep_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok2_rep_2 = keyboard.Keyboard()
    text_attractive_rep_2 = visual.TextStim(win=win, name='text_attractive_rep_2',
        text='İyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_unattractive_rep_2 = visual.TextStim(win=win, name='text_unattractive_rep_2',
        text='Kötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok2_2_rep_feedback" ---
    text_rep_feed_6 = visual.TextStim(win=win, name='text_rep_feed_6',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok5_2_inst" ---
    text_blok5_ins_2 = visual.TextStim(win=win, name='text_blok5_ins_2',
        text='\nEkrana çıkana uyaran,\n\nÖrtülü  yada  İyi ise -  E\n\nÖrtüsüz yada Kötü ise - I \n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok5_inst_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok5_2_main" ---
    target_image_blok5_3 = visual.ImageStim(
        win=win,
        name='target_image_blok5_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok5_main_2 = keyboard.Keyboard()
    text_coveredattr_main5 = visual.TextStim(win=win, name='text_coveredattr_main5',
        text='Örtülü\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncoveredunattr_main5 = visual.TextStim(win=win, name='text_uncoveredunattr_main5',
        text='Örtüsüz\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok5_2_main_feedback" ---
    text_fdb_9 = visual.TextStim(win=win, name='text_fdb_9',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok5_2_rep" ---
    target_image_blok5_rep_2 = visual.ImageStim(
        win=win,
        name='target_image_blok5_rep_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok5_rep_2 = keyboard.Keyboard()
    text_coveredattr_rep_2 = visual.TextStim(win=win, name='text_coveredattr_rep_2',
        text='Örtülü\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_uncoveredunattr_rep_2 = visual.TextStim(win=win, name='text_uncoveredunattr_rep_2',
        text='Örtüsüz\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok_5_2_rep_feedback" ---
    text_rep_feed_7 = visual.TextStim(win=win, name='text_rep_feed_7',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok1_2_inst" ---
    text_blok1_instruction1_2 = visual.TextStim(win=win, name='text_blok1_instruction1_2',
        text='Dikkat ! \n\nBaşı örtüsüz yüzler için E kullanılacak. \n\nBaşı örütülü yüzler için I kullanılacak.\n\n\nBaşlamak için boşluk tuşuna basın',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_intr1_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok1_2_main" ---
    target_image_blok1_2 = visual.ImageStim(
        win=win,
        name='target_image_blok1_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok1_main_2 = keyboard.Keyboard()
    text_uncovered_main_2 = visual.TextStim(win=win, name='text_uncovered_main_2',
        text='Örtüsüz',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_covered_main_2 = visual.TextStim(win=win, name='text_covered_main_2',
        text='Örtülü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok1_2_main_feedback" ---
    text_fdb_10 = visual.TextStim(win=win, name='text_fdb_10',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok1_2_rep" ---
    image_blok1_rep_2 = visual.ImageStim(
        win=win,
        name='image_blok1_rep_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok1_rep_2 = keyboard.Keyboard()
    text_rep_uncovered_2 = visual.TextStim(win=win, name='text_rep_uncovered_2',
        text='Örtüsüz',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_rep_covered_2 = visual.TextStim(win=win, name='text_rep_covered_2',
        text='Örtülü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok1_2_rep_feedback" ---
    text_rep_feed_8 = visual.TextStim(win=win, name='text_rep_feed_8',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok3_2_inst" ---
    text_blok3_ins_2 = visual.TextStim(win=win, name='text_blok3_ins_2',
        text='\nEkranda beliren uyaran, \n\nÖrtüsüz yada İyi ise - E \n\nÖrtülü yada Kötü - I\n\nBaşlamak için boşluk tuşuna basın ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_blok3_inst_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blok3_2_main" ---
    target_image_blok3_2 = visual.ImageStim(
        win=win,
        name='target_image_blok3_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok3_main_2 = keyboard.Keyboard()
    text_uncoveredattr_main_2 = visual.TextStim(win=win, name='text_uncoveredattr_main_2',
        text='Örtüsüz\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_coveredunattr_main_2 = visual.TextStim(win=win, name='text_coveredunattr_main_2',
        text='Örtülü\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok3_2_main_feedback" ---
    text_fdb_11 = visual.TextStim(win=win, name='text_fdb_11',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "blok3_2_rep" ---
    image_blok3_main1_rep_2 = visual.ImageStim(
        win=win,
        name='image_blok3_main1_rep_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_blok3_main1_rep_2 = keyboard.Keyboard()
    text_uncoveredattr_main_rep_2 = visual.TextStim(win=win, name='text_uncoveredattr_main_rep_2',
        text='Örtüsüz\n+\nİyi',
        font='Open Sans',
        pos=[-0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_coveredunattr_main_rep_2 = visual.TextStim(win=win, name='text_coveredunattr_main_rep_2',
        text='Örtülü\n+\nKötü',
        font='Open Sans',
        pos=[0.7, 0.4], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blok3_2_rep_feedback" ---
    text_rep_feed_9 = visual.TextStim(win=win, name='text_rep_feed_9',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "thanks2" ---
    text__thanks2 = visual.TextStim(win=win, name='text__thanks2',
        text='Katılımınız için Teşekkürler',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_thanks2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "exitcode2" ---
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "countb" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('countb.started', globalClock.getTime())
    # keep track of which components have finished
    countbComponents = []
    for thisComponent in countbComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countb" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countb" ---
    for thisComponent in countbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('countb.stopped', globalClock.getTime())
    # the Routine "countb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "general_instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('general_instruction.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    general_instructionComponents = [text_generalinst, key_resp]
    for thisComponent in general_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "general_instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_generalinst* updates
        
        # if text_generalinst is starting this frame...
        if text_generalinst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_generalinst.frameNStart = frameN  # exact frame index
            text_generalinst.tStart = t  # local t and not account for scr refresh
            text_generalinst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_generalinst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_generalinst.started')
            # update status
            text_generalinst.status = STARTED
            text_generalinst.setAutoDraw(True)
        
        # if text_generalinst is active this frame...
        if text_generalinst.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in general_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "general_instruction" ---
    for thisComponent in general_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('general_instruction.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "general_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    condition1 = data.TrialHandler(nReps=nRepsA, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition1')
    thisExp.addLoop(condition1)  # add the loop to the experiment
    thisCondition1 = condition1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
    if thisCondition1 != None:
        for paramName in thisCondition1:
            globals()[paramName] = thisCondition1[paramName]
    
    for thisCondition1 in condition1:
        currentLoop = condition1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
        if thisCondition1 != None:
            for paramName in thisCondition1:
                globals()[paramName] = thisCondition1[paramName]
        
        # --- Prepare to start Routine "blok1_instruction1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok1_instruction1.started', globalClock.getTime())
        key_resp_intr1.keys = []
        key_resp_intr1.rt = []
        _key_resp_intr1_allKeys = []
        # keep track of which components have finished
        blok1_instruction1Components = [text_blok1_instruction1, key_resp_intr1, text_uncovered0, text_Covered0]
        for thisComponent in blok1_instruction1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok1_instruction1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok1_instruction1* updates
            
            # if text_blok1_instruction1 is starting this frame...
            if text_blok1_instruction1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok1_instruction1.frameNStart = frameN  # exact frame index
                text_blok1_instruction1.tStart = t  # local t and not account for scr refresh
                text_blok1_instruction1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok1_instruction1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok1_instruction1.started')
                # update status
                text_blok1_instruction1.status = STARTED
                text_blok1_instruction1.setAutoDraw(True)
            
            # if text_blok1_instruction1 is active this frame...
            if text_blok1_instruction1.status == STARTED:
                # update params
                pass
            
            # *key_resp_intr1* updates
            waitOnFlip = False
            
            # if key_resp_intr1 is starting this frame...
            if key_resp_intr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_intr1.frameNStart = frameN  # exact frame index
                key_resp_intr1.tStart = t  # local t and not account for scr refresh
                key_resp_intr1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_intr1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_intr1.started')
                # update status
                key_resp_intr1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_intr1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_intr1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_intr1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_intr1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_intr1_allKeys.extend(theseKeys)
                if len(_key_resp_intr1_allKeys):
                    key_resp_intr1.keys = _key_resp_intr1_allKeys[-1].name  # just the last key pressed
                    key_resp_intr1.rt = _key_resp_intr1_allKeys[-1].rt
                    key_resp_intr1.duration = _key_resp_intr1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_uncovered0* updates
            
            # if text_uncovered0 is starting this frame...
            if text_uncovered0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_uncovered0.frameNStart = frameN  # exact frame index
                text_uncovered0.tStart = t  # local t and not account for scr refresh
                text_uncovered0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_uncovered0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_uncovered0.started')
                # update status
                text_uncovered0.status = STARTED
                text_uncovered0.setAutoDraw(True)
            
            # if text_uncovered0 is active this frame...
            if text_uncovered0.status == STARTED:
                # update params
                pass
            
            # *text_Covered0* updates
            
            # if text_Covered0 is starting this frame...
            if text_Covered0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Covered0.frameNStart = frameN  # exact frame index
                text_Covered0.tStart = t  # local t and not account for scr refresh
                text_Covered0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Covered0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Covered0.started')
                # update status
                text_Covered0.status = STARTED
                text_Covered0.setAutoDraw(True)
            
            # if text_Covered0 is active this frame...
            if text_Covered0.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok1_instruction1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok1_instruction1" ---
        for thisComponent in blok1_instruction1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok1_instruction1.stopped', globalClock.getTime())
        # check responses
        if key_resp_intr1.keys in ['', [], None]:  # No response was made
            key_resp_intr1.keys = None
        condition1.addData('key_resp_intr1.keys',key_resp_intr1.keys)
        if key_resp_intr1.keys != None:  # we had a response
            condition1.addData('key_resp_intr1.rt', key_resp_intr1.rt)
            condition1.addData('key_resp_intr1.duration', key_resp_intr1.duration)
        # the Routine "blok1_instruction1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_block1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Conditions1.xlsx'),
            seed=None, name='loop_block1')
        thisExp.addLoop(loop_block1)  # add the loop to the experiment
        thisLoop_block1 = loop_block1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block1.rgb)
        if thisLoop_block1 != None:
            for paramName in thisLoop_block1:
                globals()[paramName] = thisLoop_block1[paramName]
        
        for thisLoop_block1 in loop_block1:
            currentLoop = loop_block1
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block1.rgb)
            if thisLoop_block1 != None:
                for paramName in thisLoop_block1:
                    globals()[paramName] = thisLoop_block1[paramName]
            
            # --- Prepare to start Routine "Blok_1_Main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Blok_1_Main.started', globalClock.getTime())
            target_image_blok1.setImage(ImageFile)
            key_resp_blok1_main.keys = []
            key_resp_blok1_main.rt = []
            _key_resp_blok1_main_allKeys = []
            # keep track of which components have finished
            Blok_1_MainComponents = [target_image_blok1, key_resp_blok1_main, text_uncovered_main, text_covered_main]
            for thisComponent in Blok_1_MainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Blok_1_Main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok1* updates
                
                # if target_image_blok1 is starting this frame...
                if target_image_blok1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok1.frameNStart = frameN  # exact frame index
                    target_image_blok1.tStart = t  # local t and not account for scr refresh
                    target_image_blok1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok1.started')
                    # update status
                    target_image_blok1.status = STARTED
                    target_image_blok1.setAutoDraw(True)
                
                # if target_image_blok1 is active this frame...
                if target_image_blok1.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok1_main* updates
                waitOnFlip = False
                
                # if key_resp_blok1_main is starting this frame...
                if key_resp_blok1_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok1_main.frameNStart = frameN  # exact frame index
                    key_resp_blok1_main.tStart = t  # local t and not account for scr refresh
                    key_resp_blok1_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok1_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok1_main.started')
                    # update status
                    key_resp_blok1_main.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok1_main.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok1_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok1_main.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok1_main.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok1_main_allKeys.extend(theseKeys)
                    if len(_key_resp_blok1_main_allKeys):
                        key_resp_blok1_main.keys = _key_resp_blok1_main_allKeys[-1].name  # just the last key pressed
                        key_resp_blok1_main.rt = _key_resp_blok1_main_allKeys[-1].rt
                        key_resp_blok1_main.duration = _key_resp_blok1_main_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok1_main.keys == str(corrAns)) or (key_resp_blok1_main.keys == corrAns):
                            key_resp_blok1_main.corr = 1
                        else:
                            key_resp_blok1_main.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_uncovered_main* updates
                
                # if text_uncovered_main is starting this frame...
                if text_uncovered_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncovered_main.frameNStart = frameN  # exact frame index
                    text_uncovered_main.tStart = t  # local t and not account for scr refresh
                    text_uncovered_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncovered_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncovered_main.started')
                    # update status
                    text_uncovered_main.status = STARTED
                    text_uncovered_main.setAutoDraw(True)
                
                # if text_uncovered_main is active this frame...
                if text_uncovered_main.status == STARTED:
                    # update params
                    pass
                
                # *text_covered_main* updates
                
                # if text_covered_main is starting this frame...
                if text_covered_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_covered_main.frameNStart = frameN  # exact frame index
                    text_covered_main.tStart = t  # local t and not account for scr refresh
                    text_covered_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_covered_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_covered_main.started')
                    # update status
                    text_covered_main.status = STARTED
                    text_covered_main.setAutoDraw(True)
                
                # if text_covered_main is active this frame...
                if text_covered_main.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blok_1_MainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Blok_1_Main" ---
            for thisComponent in Blok_1_MainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Blok_1_Main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok1_main.keys in ['', [], None]:  # No response was made
                key_resp_blok1_main.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok1_main.corr = 1;  # correct non-response
                else:
                   key_resp_blok1_main.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_block1 (TrialHandler)
            loop_block1.addData('key_resp_blok1_main.keys',key_resp_blok1_main.keys)
            loop_block1.addData('key_resp_blok1_main.corr', key_resp_blok1_main.corr)
            if key_resp_blok1_main.keys != None:  # we had a response
                loop_block1.addData('key_resp_blok1_main.rt', key_resp_blok1_main.rt)
                loop_block1.addData('key_resp_blok1_main.duration', key_resp_blok1_main.duration)
            # Run 'End Routine' code from code_1
            if key_resp_blok1_main.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "Blok_1_Main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials')
            thisExp.addLoop(trials)  # add the loop to the experiment
            thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            for thisTrial in trials:
                currentLoop = trials
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        globals()[paramName] = thisTrial[paramName]
                
                # --- Prepare to start Routine "blok_1_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok_1_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_2
                if key_resp_blok1_main.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb.setText(fdb)
                # keep track of which components have finished
                blok_1_feedbackComponents = [text_fdb]
                for thisComponent in blok_1_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok_1_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb* updates
                    
                    # if text_fdb is starting this frame...
                    if text_fdb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb.frameNStart = frameN  # exact frame index
                        text_fdb.tStart = t  # local t and not account for scr refresh
                        text_fdb.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb.started')
                        # update status
                        text_fdb.status = STARTED
                        text_fdb.setAutoDraw(True)
                    
                    # if text_fdb is active this frame...
                    if text_fdb.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb is stopping this frame...
                    if text_fdb.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb.tStop = t  # not accounting for scr refresh
                            text_fdb.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb.stopped')
                            # update status
                            text_fdb.status = FINISHED
                            text_fdb.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok_1_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok_1_feedback" ---
                for thisComponent in blok_1_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok_1_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials'
            
            # get names of stimulus parameters
            if trials.trialList in ([], [None], None):
                params = []
            else:
                params = trials.trialList[0].keys()
            # save data for this loop
            trials.saveAsText(filename + 'trials.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_3 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_3')
            thisExp.addLoop(trials_3)  # add the loop to the experiment
            thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            
            for thisTrial_3 in trials_3:
                currentLoop = trials_3
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
                if thisTrial_3 != None:
                    for paramName in thisTrial_3:
                        globals()[paramName] = thisTrial_3[paramName]
                
                # --- Prepare to start Routine "rep_blok1" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('rep_blok1.started', globalClock.getTime())
                image_blok1_rep.setImage(ImageFile)
                key_resp_blok1_rep.keys = []
                key_resp_blok1_rep.rt = []
                _key_resp_blok1_rep_allKeys = []
                # keep track of which components have finished
                rep_blok1Components = [image_blok1_rep, key_resp_blok1_rep, text_rep_uncovered, text_rep_covered]
                for thisComponent in rep_blok1Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "rep_blok1" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_blok1_rep* updates
                    
                    # if image_blok1_rep is starting this frame...
                    if image_blok1_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_blok1_rep.frameNStart = frameN  # exact frame index
                        image_blok1_rep.tStart = t  # local t and not account for scr refresh
                        image_blok1_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_blok1_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_blok1_rep.started')
                        # update status
                        image_blok1_rep.status = STARTED
                        image_blok1_rep.setAutoDraw(True)
                    
                    # if image_blok1_rep is active this frame...
                    if image_blok1_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok1_rep* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok1_rep is starting this frame...
                    if key_resp_blok1_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok1_rep.frameNStart = frameN  # exact frame index
                        key_resp_blok1_rep.tStart = t  # local t and not account for scr refresh
                        key_resp_blok1_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok1_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok1_rep.started')
                        # update status
                        key_resp_blok1_rep.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok1_rep.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok1_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok1_rep.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok1_rep.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok1_rep_allKeys.extend(theseKeys)
                        if len(_key_resp_blok1_rep_allKeys):
                            key_resp_blok1_rep.keys = _key_resp_blok1_rep_allKeys[-1].name  # just the last key pressed
                            key_resp_blok1_rep.rt = _key_resp_blok1_rep_allKeys[-1].rt
                            key_resp_blok1_rep.duration = _key_resp_blok1_rep_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok1_rep.keys == str(corrAns)) or (key_resp_blok1_rep.keys == corrAns):
                                key_resp_blok1_rep.corr = 1
                            else:
                                key_resp_blok1_rep.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_rep_uncovered* updates
                    
                    # if text_rep_uncovered is starting this frame...
                    if text_rep_uncovered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_rep_uncovered.frameNStart = frameN  # exact frame index
                        text_rep_uncovered.tStart = t  # local t and not account for scr refresh
                        text_rep_uncovered.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_rep_uncovered, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_rep_uncovered.started')
                        # update status
                        text_rep_uncovered.status = STARTED
                        text_rep_uncovered.setAutoDraw(True)
                    
                    # if text_rep_uncovered is active this frame...
                    if text_rep_uncovered.status == STARTED:
                        # update params
                        pass
                    
                    # *text_rep_covered* updates
                    
                    # if text_rep_covered is starting this frame...
                    if text_rep_covered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_rep_covered.frameNStart = frameN  # exact frame index
                        text_rep_covered.tStart = t  # local t and not account for scr refresh
                        text_rep_covered.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_rep_covered, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_rep_covered.started')
                        # update status
                        text_rep_covered.status = STARTED
                        text_rep_covered.setAutoDraw(True)
                    
                    # if text_rep_covered is active this frame...
                    if text_rep_covered.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in rep_blok1Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "rep_blok1" ---
                for thisComponent in rep_blok1Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('rep_blok1.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok1_rep.keys in ['', [], None]:  # No response was made
                    key_resp_blok1_rep.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok1_rep.corr = 1;  # correct non-response
                    else:
                       key_resp_blok1_rep.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_3 (TrialHandler)
                trials_3.addData('key_resp_blok1_rep.keys',key_resp_blok1_rep.keys)
                trials_3.addData('key_resp_blok1_rep.corr', key_resp_blok1_rep.corr)
                if key_resp_blok1_rep.keys != None:  # we had a response
                    trials_3.addData('key_resp_blok1_rep.rt', key_resp_blok1_rep.rt)
                    trials_3.addData('key_resp_blok1_rep.duration', key_resp_blok1_rep.duration)
                # Run 'End Routine' code from code_3
                if key_resp_blok1_rep.corr == 1:
                    rep_fdb2 = 0
                    trials_3.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "rep_blok1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_2 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_2')
                thisExp.addLoop(trials_2)  # add the loop to the experiment
                thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
                if thisTrial_2 != None:
                    for paramName in thisTrial_2:
                        globals()[paramName] = thisTrial_2[paramName]
                
                for thisTrial_2 in trials_2:
                    currentLoop = trials_2
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
                    if thisTrial_2 != None:
                        for paramName in thisTrial_2:
                            globals()[paramName] = thisTrial_2[paramName]
                    
                    # --- Prepare to start Routine "blok_1_1_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok_1_1_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_4
                    if key_resp_blok1_rep.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed.setText(fdb2)
                    # keep track of which components have finished
                    blok_1_1_feedbackComponents = [text_rep_feed]
                    for thisComponent in blok_1_1_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok_1_1_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed* updates
                        
                        # if text_rep_feed is starting this frame...
                        if text_rep_feed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed.frameNStart = frameN  # exact frame index
                            text_rep_feed.tStart = t  # local t and not account for scr refresh
                            text_rep_feed.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed.started')
                            # update status
                            text_rep_feed.status = STARTED
                            text_rep_feed.setAutoDraw(True)
                        
                        # if text_rep_feed is active this frame...
                        if text_rep_feed.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed is stopping this frame...
                        if text_rep_feed.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed.tStop = t  # not accounting for scr refresh
                                text_rep_feed.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed.stopped')
                                # update status
                                text_rep_feed.status = FINISHED
                                text_rep_feed.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok_1_1_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok_1_1_feedback" ---
                    for thisComponent in blok_1_1_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok_1_1_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_2'
                
                # get names of stimulus parameters
                if trials_2.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_2.trialList[0].keys()
                # save data for this loop
                trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_3'
            
            # get names of stimulus parameters
            if trials_3.trialList in ([], [None], None):
                params = []
            else:
                params = trials_3.trialList[0].keys()
            # save data for this loop
            trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_block1'
        
        # get names of stimulus parameters
        if loop_block1.trialList in ([], [None], None):
            params = []
        else:
            params = loop_block1.trialList[0].keys()
        # save data for this loop
        loop_block1.saveAsText(filename + 'loop_block1.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok2_instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok2_instruction.started', globalClock.getTime())
        key_resp_blok2_inst.keys = []
        key_resp_blok2_inst.rt = []
        _key_resp_blok2_inst_allKeys = []
        # keep track of which components have finished
        blok2_instructionComponents = [text_blok2_inst, key_resp_blok2_inst]
        for thisComponent in blok2_instructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok2_instruction" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok2_inst* updates
            
            # if text_blok2_inst is starting this frame...
            if text_blok2_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok2_inst.frameNStart = frameN  # exact frame index
                text_blok2_inst.tStart = t  # local t and not account for scr refresh
                text_blok2_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok2_inst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok2_inst.started')
                # update status
                text_blok2_inst.status = STARTED
                text_blok2_inst.setAutoDraw(True)
            
            # if text_blok2_inst is active this frame...
            if text_blok2_inst.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok2_inst* updates
            waitOnFlip = False
            
            # if key_resp_blok2_inst is starting this frame...
            if key_resp_blok2_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok2_inst.frameNStart = frameN  # exact frame index
                key_resp_blok2_inst.tStart = t  # local t and not account for scr refresh
                key_resp_blok2_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok2_inst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok2_inst.started')
                # update status
                key_resp_blok2_inst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok2_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok2_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok2_inst.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok2_inst.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok2_inst_allKeys.extend(theseKeys)
                if len(_key_resp_blok2_inst_allKeys):
                    key_resp_blok2_inst.keys = _key_resp_blok2_inst_allKeys[-1].name  # just the last key pressed
                    key_resp_blok2_inst.rt = _key_resp_blok2_inst_allKeys[-1].rt
                    key_resp_blok2_inst.duration = _key_resp_blok2_inst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok2_instructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok2_instruction" ---
        for thisComponent in blok2_instructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok2_instruction.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok2_inst.keys in ['', [], None]:  # No response was made
            key_resp_blok2_inst.keys = None
        condition1.addData('key_resp_blok2_inst.keys',key_resp_blok2_inst.keys)
        if key_resp_blok2_inst.keys != None:  # we had a response
            condition1.addData('key_resp_blok2_inst.rt', key_resp_blok2_inst.rt)
            condition1.addData('key_resp_blok2_inst.duration', key_resp_blok2_inst.duration)
        # the Routine "blok2_instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_block2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block2Condition1.xlsx'),
            seed=None, name='loop_block2')
        thisExp.addLoop(loop_block2)  # add the loop to the experiment
        thisLoop_block2 = loop_block2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block2.rgb)
        if thisLoop_block2 != None:
            for paramName in thisLoop_block2:
                globals()[paramName] = thisLoop_block2[paramName]
        
        for thisLoop_block2 in loop_block2:
            currentLoop = loop_block2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block2.rgb)
            if thisLoop_block2 != None:
                for paramName in thisLoop_block2:
                    globals()[paramName] = thisLoop_block2[paramName]
            
            # --- Prepare to start Routine "Blok_2_Main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Blok_2_Main.started', globalClock.getTime())
            image_block2_main.setImage(wordpic)
            key_resp_blok2_main.keys = []
            key_resp_blok2_main.rt = []
            _key_resp_blok2_main_allKeys = []
            # keep track of which components have finished
            Blok_2_MainComponents = [image_block2_main, key_resp_blok2_main, text_attractive_main, text_unattractive_main]
            for thisComponent in Blok_2_MainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Blok_2_Main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_block2_main* updates
                
                # if image_block2_main is starting this frame...
                if image_block2_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_block2_main.frameNStart = frameN  # exact frame index
                    image_block2_main.tStart = t  # local t and not account for scr refresh
                    image_block2_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_block2_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block2_main.started')
                    # update status
                    image_block2_main.status = STARTED
                    image_block2_main.setAutoDraw(True)
                
                # if image_block2_main is active this frame...
                if image_block2_main.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok2_main* updates
                waitOnFlip = False
                
                # if key_resp_blok2_main is starting this frame...
                if key_resp_blok2_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok2_main.frameNStart = frameN  # exact frame index
                    key_resp_blok2_main.tStart = t  # local t and not account for scr refresh
                    key_resp_blok2_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok2_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok2_main.started')
                    # update status
                    key_resp_blok2_main.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok2_main.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok2_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok2_main.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok2_main.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok2_main_allKeys.extend(theseKeys)
                    if len(_key_resp_blok2_main_allKeys):
                        key_resp_blok2_main.keys = _key_resp_blok2_main_allKeys[-1].name  # just the last key pressed
                        key_resp_blok2_main.rt = _key_resp_blok2_main_allKeys[-1].rt
                        key_resp_blok2_main.duration = _key_resp_blok2_main_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok2_main.keys == str(corrAns)) or (key_resp_blok2_main.keys == corrAns):
                            key_resp_blok2_main.corr = 1
                        else:
                            key_resp_blok2_main.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_attractive_main* updates
                
                # if text_attractive_main is starting this frame...
                if text_attractive_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_attractive_main.frameNStart = frameN  # exact frame index
                    text_attractive_main.tStart = t  # local t and not account for scr refresh
                    text_attractive_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_attractive_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_attractive_main.started')
                    # update status
                    text_attractive_main.status = STARTED
                    text_attractive_main.setAutoDraw(True)
                
                # if text_attractive_main is active this frame...
                if text_attractive_main.status == STARTED:
                    # update params
                    pass
                
                # *text_unattractive_main* updates
                
                # if text_unattractive_main is starting this frame...
                if text_unattractive_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_unattractive_main.frameNStart = frameN  # exact frame index
                    text_unattractive_main.tStart = t  # local t and not account for scr refresh
                    text_unattractive_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_unattractive_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_unattractive_main.started')
                    # update status
                    text_unattractive_main.status = STARTED
                    text_unattractive_main.setAutoDraw(True)
                
                # if text_unattractive_main is active this frame...
                if text_unattractive_main.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blok_2_MainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Blok_2_Main" ---
            for thisComponent in Blok_2_MainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Blok_2_Main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok2_main.keys in ['', [], None]:  # No response was made
                key_resp_blok2_main.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok2_main.corr = 1;  # correct non-response
                else:
                   key_resp_blok2_main.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_block2 (TrialHandler)
            loop_block2.addData('key_resp_blok2_main.keys',key_resp_blok2_main.keys)
            loop_block2.addData('key_resp_blok2_main.corr', key_resp_blok2_main.corr)
            if key_resp_blok2_main.keys != None:  # we had a response
                loop_block2.addData('key_resp_blok2_main.rt', key_resp_blok2_main.rt)
                loop_block2.addData('key_resp_blok2_main.duration', key_resp_blok2_main.duration)
            # Run 'End Routine' code from code_5
            if key_resp_blok2_main.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "Blok_2_Main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_4 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_4')
            thisExp.addLoop(trials_4)  # add the loop to the experiment
            thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    globals()[paramName] = thisTrial_4[paramName]
            
            for thisTrial_4 in trials_4:
                currentLoop = trials_4
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
                if thisTrial_4 != None:
                    for paramName in thisTrial_4:
                        globals()[paramName] = thisTrial_4[paramName]
                
                # --- Prepare to start Routine "blok_2_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok_2_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_6
                if key_resp_blok2_main.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_2.setText(fdb)
                # keep track of which components have finished
                blok_2_feedbackComponents = [text_fdb_2]
                for thisComponent in blok_2_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok_2_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_2* updates
                    
                    # if text_fdb_2 is starting this frame...
                    if text_fdb_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_2.frameNStart = frameN  # exact frame index
                        text_fdb_2.tStart = t  # local t and not account for scr refresh
                        text_fdb_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_2.started')
                        # update status
                        text_fdb_2.status = STARTED
                        text_fdb_2.setAutoDraw(True)
                    
                    # if text_fdb_2 is active this frame...
                    if text_fdb_2.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_2 is stopping this frame...
                    if text_fdb_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_2.tStop = t  # not accounting for scr refresh
                            text_fdb_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_2.stopped')
                            # update status
                            text_fdb_2.status = FINISHED
                            text_fdb_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok_2_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok_2_feedback" ---
                for thisComponent in blok_2_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok_2_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_4'
            
            # get names of stimulus parameters
            if trials_4.trialList in ([], [None], None):
                params = []
            else:
                params = trials_4.trialList[0].keys()
            # save data for this loop
            trials_4.saveAsText(filename + 'trials_4.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_6 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_6')
            thisExp.addLoop(trials_6)  # add the loop to the experiment
            thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
            if thisTrial_6 != None:
                for paramName in thisTrial_6:
                    globals()[paramName] = thisTrial_6[paramName]
            
            for thisTrial_6 in trials_6:
                currentLoop = trials_6
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
                if thisTrial_6 != None:
                    for paramName in thisTrial_6:
                        globals()[paramName] = thisTrial_6[paramName]
                
                # --- Prepare to start Routine "rep_blok2" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('rep_blok2.started', globalClock.getTime())
                image_block2_rep.setImage(wordpic)
                key_resp_blok2_rep.keys = []
                key_resp_blok2_rep.rt = []
                _key_resp_blok2_rep_allKeys = []
                # keep track of which components have finished
                rep_blok2Components = [image_block2_rep, key_resp_blok2_rep, text_attractive_rep, text_unattractive_rep]
                for thisComponent in rep_blok2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "rep_blok2" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_block2_rep* updates
                    
                    # if image_block2_rep is starting this frame...
                    if image_block2_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_block2_rep.frameNStart = frameN  # exact frame index
                        image_block2_rep.tStart = t  # local t and not account for scr refresh
                        image_block2_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_block2_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_block2_rep.started')
                        # update status
                        image_block2_rep.status = STARTED
                        image_block2_rep.setAutoDraw(True)
                    
                    # if image_block2_rep is active this frame...
                    if image_block2_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok2_rep* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok2_rep is starting this frame...
                    if key_resp_blok2_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok2_rep.frameNStart = frameN  # exact frame index
                        key_resp_blok2_rep.tStart = t  # local t and not account for scr refresh
                        key_resp_blok2_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok2_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok2_rep.started')
                        # update status
                        key_resp_blok2_rep.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok2_rep.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok2_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok2_rep.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok2_rep.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok2_rep_allKeys.extend(theseKeys)
                        if len(_key_resp_blok2_rep_allKeys):
                            key_resp_blok2_rep.keys = _key_resp_blok2_rep_allKeys[-1].name  # just the last key pressed
                            key_resp_blok2_rep.rt = _key_resp_blok2_rep_allKeys[-1].rt
                            key_resp_blok2_rep.duration = _key_resp_blok2_rep_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok2_rep.keys == str(corrAns)) or (key_resp_blok2_rep.keys == corrAns):
                                key_resp_blok2_rep.corr = 1
                            else:
                                key_resp_blok2_rep.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_attractive_rep* updates
                    
                    # if text_attractive_rep is starting this frame...
                    if text_attractive_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_attractive_rep.frameNStart = frameN  # exact frame index
                        text_attractive_rep.tStart = t  # local t and not account for scr refresh
                        text_attractive_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_attractive_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_attractive_rep.started')
                        # update status
                        text_attractive_rep.status = STARTED
                        text_attractive_rep.setAutoDraw(True)
                    
                    # if text_attractive_rep is active this frame...
                    if text_attractive_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *text_unattractive_rep* updates
                    
                    # if text_unattractive_rep is starting this frame...
                    if text_unattractive_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_unattractive_rep.frameNStart = frameN  # exact frame index
                        text_unattractive_rep.tStart = t  # local t and not account for scr refresh
                        text_unattractive_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_unattractive_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_unattractive_rep.started')
                        # update status
                        text_unattractive_rep.status = STARTED
                        text_unattractive_rep.setAutoDraw(True)
                    
                    # if text_unattractive_rep is active this frame...
                    if text_unattractive_rep.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in rep_blok2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "rep_blok2" ---
                for thisComponent in rep_blok2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('rep_blok2.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok2_rep.keys in ['', [], None]:  # No response was made
                    key_resp_blok2_rep.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok2_rep.corr = 1;  # correct non-response
                    else:
                       key_resp_blok2_rep.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_6 (TrialHandler)
                trials_6.addData('key_resp_blok2_rep.keys',key_resp_blok2_rep.keys)
                trials_6.addData('key_resp_blok2_rep.corr', key_resp_blok2_rep.corr)
                if key_resp_blok2_rep.keys != None:  # we had a response
                    trials_6.addData('key_resp_blok2_rep.rt', key_resp_blok2_rep.rt)
                    trials_6.addData('key_resp_blok2_rep.duration', key_resp_blok2_rep.duration)
                # Run 'End Routine' code from code_7
                if key_resp_blok2_rep.corr == 1:
                    rep_fdb2 = 0
                    trials_6.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "rep_blok2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_5 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_5')
                thisExp.addLoop(trials_5)  # add the loop to the experiment
                thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
                if thisTrial_5 != None:
                    for paramName in thisTrial_5:
                        globals()[paramName] = thisTrial_5[paramName]
                
                for thisTrial_5 in trials_5:
                    currentLoop = trials_5
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
                    if thisTrial_5 != None:
                        for paramName in thisTrial_5:
                            globals()[paramName] = thisTrial_5[paramName]
                    
                    # --- Prepare to start Routine "blok_2_1_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok_2_1_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_8
                    if key_resp_blok2_rep.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_2.setText(fdb2)
                    # keep track of which components have finished
                    blok_2_1_feedbackComponents = [text_rep_feed_2]
                    for thisComponent in blok_2_1_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok_2_1_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_2* updates
                        
                        # if text_rep_feed_2 is starting this frame...
                        if text_rep_feed_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_2.frameNStart = frameN  # exact frame index
                            text_rep_feed_2.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_2, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_2.started')
                            # update status
                            text_rep_feed_2.status = STARTED
                            text_rep_feed_2.setAutoDraw(True)
                        
                        # if text_rep_feed_2 is active this frame...
                        if text_rep_feed_2.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_2 is stopping this frame...
                        if text_rep_feed_2.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_2.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_2.tStop = t  # not accounting for scr refresh
                                text_rep_feed_2.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_2.stopped')
                                # update status
                                text_rep_feed_2.status = FINISHED
                                text_rep_feed_2.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok_2_1_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok_2_1_feedback" ---
                    for thisComponent in blok_2_1_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok_2_1_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_5'
                
                # get names of stimulus parameters
                if trials_5.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_5.trialList[0].keys()
                # save data for this loop
                trials_5.saveAsText(filename + 'trials_5.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_6'
            
            # get names of stimulus parameters
            if trials_6.trialList in ([], [None], None):
                params = []
            else:
                params = trials_6.trialList[0].keys()
            # save data for this loop
            trials_6.saveAsText(filename + 'trials_6.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_block2'
        
        # get names of stimulus parameters
        if loop_block2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_block2.trialList[0].keys()
        # save data for this loop
        loop_block2.saveAsText(filename + 'loop_block2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok_3_instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok_3_instruction.started', globalClock.getTime())
        key_resp_blok3_inst.keys = []
        key_resp_blok3_inst.rt = []
        _key_resp_blok3_inst_allKeys = []
        # keep track of which components have finished
        blok_3_instructionComponents = [text_blok3_ins, key_resp_blok3_inst]
        for thisComponent in blok_3_instructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok_3_instruction" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok3_ins* updates
            
            # if text_blok3_ins is starting this frame...
            if text_blok3_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok3_ins.frameNStart = frameN  # exact frame index
                text_blok3_ins.tStart = t  # local t and not account for scr refresh
                text_blok3_ins.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok3_ins, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok3_ins.started')
                # update status
                text_blok3_ins.status = STARTED
                text_blok3_ins.setAutoDraw(True)
            
            # if text_blok3_ins is active this frame...
            if text_blok3_ins.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok3_inst* updates
            waitOnFlip = False
            
            # if key_resp_blok3_inst is starting this frame...
            if key_resp_blok3_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok3_inst.frameNStart = frameN  # exact frame index
                key_resp_blok3_inst.tStart = t  # local t and not account for scr refresh
                key_resp_blok3_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok3_inst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok3_inst.started')
                # update status
                key_resp_blok3_inst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok3_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok3_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok3_inst.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok3_inst.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok3_inst_allKeys.extend(theseKeys)
                if len(_key_resp_blok3_inst_allKeys):
                    key_resp_blok3_inst.keys = _key_resp_blok3_inst_allKeys[-1].name  # just the last key pressed
                    key_resp_blok3_inst.rt = _key_resp_blok3_inst_allKeys[-1].rt
                    key_resp_blok3_inst.duration = _key_resp_blok3_inst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok_3_instructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok_3_instruction" ---
        for thisComponent in blok_3_instructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok_3_instruction.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok3_inst.keys in ['', [], None]:  # No response was made
            key_resp_blok3_inst.keys = None
        condition1.addData('key_resp_blok3_inst.keys',key_resp_blok3_inst.keys)
        if key_resp_blok3_inst.keys != None:  # we had a response
            condition1.addData('key_resp_blok3_inst.rt', key_resp_blok3_inst.rt)
            condition1.addData('key_resp_blok3_inst.duration', key_resp_blok3_inst.duration)
        # the Routine "blok_3_instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_block3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block3Condition1.xlsx'),
            seed=None, name='loop_block3')
        thisExp.addLoop(loop_block3)  # add the loop to the experiment
        thisLoop_block3 = loop_block3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block3.rgb)
        if thisLoop_block3 != None:
            for paramName in thisLoop_block3:
                globals()[paramName] = thisLoop_block3[paramName]
        
        for thisLoop_block3 in loop_block3:
            currentLoop = loop_block3
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block3.rgb)
            if thisLoop_block3 != None:
                for paramName in thisLoop_block3:
                    globals()[paramName] = thisLoop_block3[paramName]
            
            # --- Prepare to start Routine "blok_3_main1" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok_3_main1.started', globalClock.getTime())
            target_image_blok3.setImage(ImageFiles)
            key_resp_blok3_main_1.keys = []
            key_resp_blok3_main_1.rt = []
            _key_resp_blok3_main_1_allKeys = []
            # keep track of which components have finished
            blok_3_main1Components = [target_image_blok3, key_resp_blok3_main_1, text_uncoveredattr_main, text_coveredunattr_main]
            for thisComponent in blok_3_main1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok_3_main1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok3* updates
                
                # if target_image_blok3 is starting this frame...
                if target_image_blok3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok3.frameNStart = frameN  # exact frame index
                    target_image_blok3.tStart = t  # local t and not account for scr refresh
                    target_image_blok3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok3.started')
                    # update status
                    target_image_blok3.status = STARTED
                    target_image_blok3.setAutoDraw(True)
                
                # if target_image_blok3 is active this frame...
                if target_image_blok3.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok3_main_1* updates
                waitOnFlip = False
                
                # if key_resp_blok3_main_1 is starting this frame...
                if key_resp_blok3_main_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok3_main_1.frameNStart = frameN  # exact frame index
                    key_resp_blok3_main_1.tStart = t  # local t and not account for scr refresh
                    key_resp_blok3_main_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok3_main_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok3_main_1.started')
                    # update status
                    key_resp_blok3_main_1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok3_main_1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok3_main_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok3_main_1.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok3_main_1.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok3_main_1_allKeys.extend(theseKeys)
                    if len(_key_resp_blok3_main_1_allKeys):
                        key_resp_blok3_main_1.keys = _key_resp_blok3_main_1_allKeys[-1].name  # just the last key pressed
                        key_resp_blok3_main_1.rt = _key_resp_blok3_main_1_allKeys[-1].rt
                        key_resp_blok3_main_1.duration = _key_resp_blok3_main_1_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok3_main_1.keys == str(corrAns)) or (key_resp_blok3_main_1.keys == corrAns):
                            key_resp_blok3_main_1.corr = 1
                        else:
                            key_resp_blok3_main_1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_uncoveredattr_main* updates
                
                # if text_uncoveredattr_main is starting this frame...
                if text_uncoveredattr_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncoveredattr_main.frameNStart = frameN  # exact frame index
                    text_uncoveredattr_main.tStart = t  # local t and not account for scr refresh
                    text_uncoveredattr_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncoveredattr_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncoveredattr_main.started')
                    # update status
                    text_uncoveredattr_main.status = STARTED
                    text_uncoveredattr_main.setAutoDraw(True)
                
                # if text_uncoveredattr_main is active this frame...
                if text_uncoveredattr_main.status == STARTED:
                    # update params
                    pass
                
                # *text_coveredunattr_main* updates
                
                # if text_coveredunattr_main is starting this frame...
                if text_coveredunattr_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_coveredunattr_main.frameNStart = frameN  # exact frame index
                    text_coveredunattr_main.tStart = t  # local t and not account for scr refresh
                    text_coveredunattr_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_coveredunattr_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_coveredunattr_main.started')
                    # update status
                    text_coveredunattr_main.status = STARTED
                    text_coveredunattr_main.setAutoDraw(True)
                
                # if text_coveredunattr_main is active this frame...
                if text_coveredunattr_main.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok_3_main1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok_3_main1" ---
            for thisComponent in blok_3_main1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok_3_main1.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok3_main_1.keys in ['', [], None]:  # No response was made
                key_resp_blok3_main_1.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok3_main_1.corr = 1;  # correct non-response
                else:
                   key_resp_blok3_main_1.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_block3 (TrialHandler)
            loop_block3.addData('key_resp_blok3_main_1.keys',key_resp_blok3_main_1.keys)
            loop_block3.addData('key_resp_blok3_main_1.corr', key_resp_blok3_main_1.corr)
            if key_resp_blok3_main_1.keys != None:  # we had a response
                loop_block3.addData('key_resp_blok3_main_1.rt', key_resp_blok3_main_1.rt)
                loop_block3.addData('key_resp_blok3_main_1.duration', key_resp_blok3_main_1.duration)
            # Run 'End Routine' code from code_10
            if key_resp_blok3_main_1.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok_3_main1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_7 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_7')
            thisExp.addLoop(trials_7)  # add the loop to the experiment
            thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
            if thisTrial_7 != None:
                for paramName in thisTrial_7:
                    globals()[paramName] = thisTrial_7[paramName]
            
            for thisTrial_7 in trials_7:
                currentLoop = trials_7
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
                if thisTrial_7 != None:
                    for paramName in thisTrial_7:
                        globals()[paramName] = thisTrial_7[paramName]
                
                # --- Prepare to start Routine "blok3_main1_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok3_main1_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code
                if key_resp_blok3_main_1.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_3.setText(fdb)
                # keep track of which components have finished
                blok3_main1_feedbackComponents = [text_fdb_3]
                for thisComponent in blok3_main1_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok3_main1_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_3* updates
                    
                    # if text_fdb_3 is starting this frame...
                    if text_fdb_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_3.frameNStart = frameN  # exact frame index
                        text_fdb_3.tStart = t  # local t and not account for scr refresh
                        text_fdb_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_3.started')
                        # update status
                        text_fdb_3.status = STARTED
                        text_fdb_3.setAutoDraw(True)
                    
                    # if text_fdb_3 is active this frame...
                    if text_fdb_3.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_3 is stopping this frame...
                    if text_fdb_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_3.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_3.tStop = t  # not accounting for scr refresh
                            text_fdb_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_3.stopped')
                            # update status
                            text_fdb_3.status = FINISHED
                            text_fdb_3.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok3_main1_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok3_main1_feedback" ---
                for thisComponent in blok3_main1_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok3_main1_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_7'
            
            # get names of stimulus parameters
            if trials_7.trialList in ([], [None], None):
                params = []
            else:
                params = trials_7.trialList[0].keys()
            # save data for this loop
            trials_7.saveAsText(filename + 'trials_7.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_9 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_9')
            thisExp.addLoop(trials_9)  # add the loop to the experiment
            thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
            if thisTrial_9 != None:
                for paramName in thisTrial_9:
                    globals()[paramName] = thisTrial_9[paramName]
            
            for thisTrial_9 in trials_9:
                currentLoop = trials_9
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
                if thisTrial_9 != None:
                    for paramName in thisTrial_9:
                        globals()[paramName] = thisTrial_9[paramName]
                
                # --- Prepare to start Routine "blok3_main1_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok3_main1_rep.started', globalClock.getTime())
                image_blok3_main1_rep.setImage(ImageFiles)
                key_resp_blok3_main1_rep.keys = []
                key_resp_blok3_main1_rep.rt = []
                _key_resp_blok3_main1_rep_allKeys = []
                # keep track of which components have finished
                blok3_main1_repComponents = [image_blok3_main1_rep, key_resp_blok3_main1_rep, text_uncoveredattr_main_rep, text_coveredunattr_main_rep]
                for thisComponent in blok3_main1_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok3_main1_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_blok3_main1_rep* updates
                    
                    # if image_blok3_main1_rep is starting this frame...
                    if image_blok3_main1_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_blok3_main1_rep.frameNStart = frameN  # exact frame index
                        image_blok3_main1_rep.tStart = t  # local t and not account for scr refresh
                        image_blok3_main1_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_blok3_main1_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_blok3_main1_rep.started')
                        # update status
                        image_blok3_main1_rep.status = STARTED
                        image_blok3_main1_rep.setAutoDraw(True)
                    
                    # if image_blok3_main1_rep is active this frame...
                    if image_blok3_main1_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok3_main1_rep* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok3_main1_rep is starting this frame...
                    if key_resp_blok3_main1_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok3_main1_rep.frameNStart = frameN  # exact frame index
                        key_resp_blok3_main1_rep.tStart = t  # local t and not account for scr refresh
                        key_resp_blok3_main1_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok3_main1_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok3_main1_rep.started')
                        # update status
                        key_resp_blok3_main1_rep.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok3_main1_rep.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok3_main1_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok3_main1_rep.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok3_main1_rep.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok3_main1_rep_allKeys.extend(theseKeys)
                        if len(_key_resp_blok3_main1_rep_allKeys):
                            key_resp_blok3_main1_rep.keys = _key_resp_blok3_main1_rep_allKeys[-1].name  # just the last key pressed
                            key_resp_blok3_main1_rep.rt = _key_resp_blok3_main1_rep_allKeys[-1].rt
                            key_resp_blok3_main1_rep.duration = _key_resp_blok3_main1_rep_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok3_main1_rep.keys == str(corrAns)) or (key_resp_blok3_main1_rep.keys == corrAns):
                                key_resp_blok3_main1_rep.corr = 1
                            else:
                                key_resp_blok3_main1_rep.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_uncoveredattr_main_rep* updates
                    
                    # if text_uncoveredattr_main_rep is starting this frame...
                    if text_uncoveredattr_main_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncoveredattr_main_rep.frameNStart = frameN  # exact frame index
                        text_uncoveredattr_main_rep.tStart = t  # local t and not account for scr refresh
                        text_uncoveredattr_main_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncoveredattr_main_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncoveredattr_main_rep.started')
                        # update status
                        text_uncoveredattr_main_rep.status = STARTED
                        text_uncoveredattr_main_rep.setAutoDraw(True)
                    
                    # if text_uncoveredattr_main_rep is active this frame...
                    if text_uncoveredattr_main_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *text_coveredunattr_main_rep* updates
                    
                    # if text_coveredunattr_main_rep is starting this frame...
                    if text_coveredunattr_main_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_coveredunattr_main_rep.frameNStart = frameN  # exact frame index
                        text_coveredunattr_main_rep.tStart = t  # local t and not account for scr refresh
                        text_coveredunattr_main_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_coveredunattr_main_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_coveredunattr_main_rep.started')
                        # update status
                        text_coveredunattr_main_rep.status = STARTED
                        text_coveredunattr_main_rep.setAutoDraw(True)
                    
                    # if text_coveredunattr_main_rep is active this frame...
                    if text_coveredunattr_main_rep.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok3_main1_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok3_main1_rep" ---
                for thisComponent in blok3_main1_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok3_main1_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok3_main1_rep.keys in ['', [], None]:  # No response was made
                    key_resp_blok3_main1_rep.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok3_main1_rep.corr = 1;  # correct non-response
                    else:
                       key_resp_blok3_main1_rep.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_9 (TrialHandler)
                trials_9.addData('key_resp_blok3_main1_rep.keys',key_resp_blok3_main1_rep.keys)
                trials_9.addData('key_resp_blok3_main1_rep.corr', key_resp_blok3_main1_rep.corr)
                if key_resp_blok3_main1_rep.keys != None:  # we had a response
                    trials_9.addData('key_resp_blok3_main1_rep.rt', key_resp_blok3_main1_rep.rt)
                    trials_9.addData('key_resp_blok3_main1_rep.duration', key_resp_blok3_main1_rep.duration)
                # Run 'End Routine' code from code_9
                if key_resp_blok3_main1_rep.corr == 1:
                    rep_fdb2 = 0
                    trials_9.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok3_main1_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_8 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_8')
                thisExp.addLoop(trials_8)  # add the loop to the experiment
                thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
                if thisTrial_8 != None:
                    for paramName in thisTrial_8:
                        globals()[paramName] = thisTrial_8[paramName]
                
                for thisTrial_8 in trials_8:
                    currentLoop = trials_8
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
                    if thisTrial_8 != None:
                        for paramName in thisTrial_8:
                            globals()[paramName] = thisTrial_8[paramName]
                    
                    # --- Prepare to start Routine "blok3_main1_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok3_main1_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_11
                    if key_resp_blok3_main1_rep.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_3.setText(fdb2)
                    # keep track of which components have finished
                    blok3_main1_rep_feedbackComponents = [text_rep_feed_3]
                    for thisComponent in blok3_main1_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok3_main1_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_3* updates
                        
                        # if text_rep_feed_3 is starting this frame...
                        if text_rep_feed_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_3.frameNStart = frameN  # exact frame index
                            text_rep_feed_3.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_3.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_3, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_3.started')
                            # update status
                            text_rep_feed_3.status = STARTED
                            text_rep_feed_3.setAutoDraw(True)
                        
                        # if text_rep_feed_3 is active this frame...
                        if text_rep_feed_3.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_3 is stopping this frame...
                        if text_rep_feed_3.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_3.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_3.tStop = t  # not accounting for scr refresh
                                text_rep_feed_3.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_3.stopped')
                                # update status
                                text_rep_feed_3.status = FINISHED
                                text_rep_feed_3.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok3_main1_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok3_main1_rep_feedback" ---
                    for thisComponent in blok3_main1_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok3_main1_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_8'
                
                # get names of stimulus parameters
                if trials_8.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_8.trialList[0].keys()
                # save data for this loop
                trials_8.saveAsText(filename + 'trials_8.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_9'
            
            # get names of stimulus parameters
            if trials_9.trialList in ([], [None], None):
                params = []
            else:
                params = trials_9.trialList[0].keys()
            # save data for this loop
            trials_9.saveAsText(filename + 'trials_9.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_block3'
        
        # get names of stimulus parameters
        if loop_block3.trialList in ([], [None], None):
            params = []
        else:
            params = loop_block3.trialList[0].keys()
        # save data for this loop
        loop_block3.saveAsText(filename + 'loop_block3.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok_4_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok_4_inst.started', globalClock.getTime())
        key_resp_blok4_inst.keys = []
        key_resp_blok4_inst.rt = []
        _key_resp_blok4_inst_allKeys = []
        # keep track of which components have finished
        blok_4_instComponents = [text_blok4_ins, key_resp_blok4_inst]
        for thisComponent in blok_4_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok_4_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok4_ins* updates
            
            # if text_blok4_ins is starting this frame...
            if text_blok4_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok4_ins.frameNStart = frameN  # exact frame index
                text_blok4_ins.tStart = t  # local t and not account for scr refresh
                text_blok4_ins.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok4_ins, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok4_ins.started')
                # update status
                text_blok4_ins.status = STARTED
                text_blok4_ins.setAutoDraw(True)
            
            # if text_blok4_ins is active this frame...
            if text_blok4_ins.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok4_inst* updates
            waitOnFlip = False
            
            # if key_resp_blok4_inst is starting this frame...
            if key_resp_blok4_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok4_inst.frameNStart = frameN  # exact frame index
                key_resp_blok4_inst.tStart = t  # local t and not account for scr refresh
                key_resp_blok4_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok4_inst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok4_inst.started')
                # update status
                key_resp_blok4_inst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok4_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok4_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok4_inst.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok4_inst.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok4_inst_allKeys.extend(theseKeys)
                if len(_key_resp_blok4_inst_allKeys):
                    key_resp_blok4_inst.keys = _key_resp_blok4_inst_allKeys[-1].name  # just the last key pressed
                    key_resp_blok4_inst.rt = _key_resp_blok4_inst_allKeys[-1].rt
                    key_resp_blok4_inst.duration = _key_resp_blok4_inst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok_4_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok_4_inst" ---
        for thisComponent in blok_4_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok_4_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok4_inst.keys in ['', [], None]:  # No response was made
            key_resp_blok4_inst.keys = None
        condition1.addData('key_resp_blok4_inst.keys',key_resp_blok4_inst.keys)
        if key_resp_blok4_inst.keys != None:  # we had a response
            condition1.addData('key_resp_blok4_inst.rt', key_resp_blok4_inst.rt)
            condition1.addData('key_resp_blok4_inst.duration', key_resp_blok4_inst.duration)
        # the Routine "blok_4_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_block4 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block4Condition1.xlsx'),
            seed=None, name='loop_block4')
        thisExp.addLoop(loop_block4)  # add the loop to the experiment
        thisLoop_block4 = loop_block4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block4.rgb)
        if thisLoop_block4 != None:
            for paramName in thisLoop_block4:
                globals()[paramName] = thisLoop_block4[paramName]
        
        for thisLoop_block4 in loop_block4:
            currentLoop = loop_block4
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block4.rgb)
            if thisLoop_block4 != None:
                for paramName in thisLoop_block4:
                    globals()[paramName] = thisLoop_block4[paramName]
            
            # --- Prepare to start Routine "blok4_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok4_main.started', globalClock.getTime())
            target_image_blok4.setImage(ImageFiles)
            key_resp_blok4_main.keys = []
            key_resp_blok4_main.rt = []
            _key_resp_blok4_main_allKeys = []
            # keep track of which components have finished
            blok4_mainComponents = [target_image_blok4, key_resp_blok4_main, text_covered_main_4, text_uncovered_main_4]
            for thisComponent in blok4_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok4_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok4* updates
                
                # if target_image_blok4 is starting this frame...
                if target_image_blok4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok4.frameNStart = frameN  # exact frame index
                    target_image_blok4.tStart = t  # local t and not account for scr refresh
                    target_image_blok4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok4.started')
                    # update status
                    target_image_blok4.status = STARTED
                    target_image_blok4.setAutoDraw(True)
                
                # if target_image_blok4 is active this frame...
                if target_image_blok4.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok4_main* updates
                waitOnFlip = False
                
                # if key_resp_blok4_main is starting this frame...
                if key_resp_blok4_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok4_main.frameNStart = frameN  # exact frame index
                    key_resp_blok4_main.tStart = t  # local t and not account for scr refresh
                    key_resp_blok4_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok4_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok4_main.started')
                    # update status
                    key_resp_blok4_main.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok4_main.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok4_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok4_main.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok4_main.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok4_main_allKeys.extend(theseKeys)
                    if len(_key_resp_blok4_main_allKeys):
                        key_resp_blok4_main.keys = _key_resp_blok4_main_allKeys[-1].name  # just the last key pressed
                        key_resp_blok4_main.rt = _key_resp_blok4_main_allKeys[-1].rt
                        key_resp_blok4_main.duration = _key_resp_blok4_main_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok4_main.keys == str(corrAns)) or (key_resp_blok4_main.keys == corrAns):
                            key_resp_blok4_main.corr = 1
                        else:
                            key_resp_blok4_main.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_covered_main_4* updates
                
                # if text_covered_main_4 is starting this frame...
                if text_covered_main_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_covered_main_4.frameNStart = frameN  # exact frame index
                    text_covered_main_4.tStart = t  # local t and not account for scr refresh
                    text_covered_main_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_covered_main_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_covered_main_4.started')
                    # update status
                    text_covered_main_4.status = STARTED
                    text_covered_main_4.setAutoDraw(True)
                
                # if text_covered_main_4 is active this frame...
                if text_covered_main_4.status == STARTED:
                    # update params
                    pass
                
                # *text_uncovered_main_4* updates
                
                # if text_uncovered_main_4 is starting this frame...
                if text_uncovered_main_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncovered_main_4.frameNStart = frameN  # exact frame index
                    text_uncovered_main_4.tStart = t  # local t and not account for scr refresh
                    text_uncovered_main_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncovered_main_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncovered_main_4.started')
                    # update status
                    text_uncovered_main_4.status = STARTED
                    text_uncovered_main_4.setAutoDraw(True)
                
                # if text_uncovered_main_4 is active this frame...
                if text_uncovered_main_4.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok4_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok4_main" ---
            for thisComponent in blok4_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok4_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok4_main.keys in ['', [], None]:  # No response was made
                key_resp_blok4_main.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok4_main.corr = 1;  # correct non-response
                else:
                   key_resp_blok4_main.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_block4 (TrialHandler)
            loop_block4.addData('key_resp_blok4_main.keys',key_resp_blok4_main.keys)
            loop_block4.addData('key_resp_blok4_main.corr', key_resp_blok4_main.corr)
            if key_resp_blok4_main.keys != None:  # we had a response
                loop_block4.addData('key_resp_blok4_main.rt', key_resp_blok4_main.rt)
                loop_block4.addData('key_resp_blok4_main.duration', key_resp_blok4_main.duration)
            # Run 'End Routine' code from code_14
            if key_resp_blok4_main.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok4_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_11 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_11')
            thisExp.addLoop(trials_11)  # add the loop to the experiment
            thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
            if thisTrial_11 != None:
                for paramName in thisTrial_11:
                    globals()[paramName] = thisTrial_11[paramName]
            
            for thisTrial_11 in trials_11:
                currentLoop = trials_11
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
                if thisTrial_11 != None:
                    for paramName in thisTrial_11:
                        globals()[paramName] = thisTrial_11[paramName]
                
                # --- Prepare to start Routine "blok4_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok4_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_15
                if key_resp_blok4_main.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_5.setText(fdb)
                # keep track of which components have finished
                blok4_main_feedbackComponents = [text_fdb_5]
                for thisComponent in blok4_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok4_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_5* updates
                    
                    # if text_fdb_5 is starting this frame...
                    if text_fdb_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_5.frameNStart = frameN  # exact frame index
                        text_fdb_5.tStart = t  # local t and not account for scr refresh
                        text_fdb_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_5.started')
                        # update status
                        text_fdb_5.status = STARTED
                        text_fdb_5.setAutoDraw(True)
                    
                    # if text_fdb_5 is active this frame...
                    if text_fdb_5.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_5 is stopping this frame...
                    if text_fdb_5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_5.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_5.tStop = t  # not accounting for scr refresh
                            text_fdb_5.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_5.stopped')
                            # update status
                            text_fdb_5.status = FINISHED
                            text_fdb_5.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok4_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok4_main_feedback" ---
                for thisComponent in blok4_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok4_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_11'
            
            # get names of stimulus parameters
            if trials_11.trialList in ([], [None], None):
                params = []
            else:
                params = trials_11.trialList[0].keys()
            # save data for this loop
            trials_11.saveAsText(filename + 'trials_11.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_14 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_14')
            thisExp.addLoop(trials_14)  # add the loop to the experiment
            thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
            if thisTrial_14 != None:
                for paramName in thisTrial_14:
                    globals()[paramName] = thisTrial_14[paramName]
            
            for thisTrial_14 in trials_14:
                currentLoop = trials_14
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
                if thisTrial_14 != None:
                    for paramName in thisTrial_14:
                        globals()[paramName] = thisTrial_14[paramName]
                
                # --- Prepare to start Routine "blok4_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok4_rep.started', globalClock.getTime())
                target_image_blok4_rep.setImage(ImageFiles)
                key_resp_blok4_rep.keys = []
                key_resp_blok4_rep.rt = []
                _key_resp_blok4_rep_allKeys = []
                # keep track of which components have finished
                blok4_repComponents = [target_image_blok4_rep, key_resp_blok4_rep, text_covered_rep_4, text_uncovered_rep_4]
                for thisComponent in blok4_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok4_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *target_image_blok4_rep* updates
                    
                    # if target_image_blok4_rep is starting this frame...
                    if target_image_blok4_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        target_image_blok4_rep.frameNStart = frameN  # exact frame index
                        target_image_blok4_rep.tStart = t  # local t and not account for scr refresh
                        target_image_blok4_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_image_blok4_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_image_blok4_rep.started')
                        # update status
                        target_image_blok4_rep.status = STARTED
                        target_image_blok4_rep.setAutoDraw(True)
                    
                    # if target_image_blok4_rep is active this frame...
                    if target_image_blok4_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok4_rep* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok4_rep is starting this frame...
                    if key_resp_blok4_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok4_rep.frameNStart = frameN  # exact frame index
                        key_resp_blok4_rep.tStart = t  # local t and not account for scr refresh
                        key_resp_blok4_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok4_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok4_rep.started')
                        # update status
                        key_resp_blok4_rep.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok4_rep.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok4_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok4_rep.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok4_rep.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok4_rep_allKeys.extend(theseKeys)
                        if len(_key_resp_blok4_rep_allKeys):
                            key_resp_blok4_rep.keys = _key_resp_blok4_rep_allKeys[-1].name  # just the last key pressed
                            key_resp_blok4_rep.rt = _key_resp_blok4_rep_allKeys[-1].rt
                            key_resp_blok4_rep.duration = _key_resp_blok4_rep_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok4_rep.keys == str(corrAns)) or (key_resp_blok4_rep.keys == corrAns):
                                key_resp_blok4_rep.corr = 1
                            else:
                                key_resp_blok4_rep.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_covered_rep_4* updates
                    
                    # if text_covered_rep_4 is starting this frame...
                    if text_covered_rep_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_covered_rep_4.frameNStart = frameN  # exact frame index
                        text_covered_rep_4.tStart = t  # local t and not account for scr refresh
                        text_covered_rep_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_covered_rep_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_covered_rep_4.started')
                        # update status
                        text_covered_rep_4.status = STARTED
                        text_covered_rep_4.setAutoDraw(True)
                    
                    # if text_covered_rep_4 is active this frame...
                    if text_covered_rep_4.status == STARTED:
                        # update params
                        pass
                    
                    # *text_uncovered_rep_4* updates
                    
                    # if text_uncovered_rep_4 is starting this frame...
                    if text_uncovered_rep_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncovered_rep_4.frameNStart = frameN  # exact frame index
                        text_uncovered_rep_4.tStart = t  # local t and not account for scr refresh
                        text_uncovered_rep_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncovered_rep_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncovered_rep_4.started')
                        # update status
                        text_uncovered_rep_4.status = STARTED
                        text_uncovered_rep_4.setAutoDraw(True)
                    
                    # if text_uncovered_rep_4 is active this frame...
                    if text_uncovered_rep_4.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok4_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok4_rep" ---
                for thisComponent in blok4_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok4_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok4_rep.keys in ['', [], None]:  # No response was made
                    key_resp_blok4_rep.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok4_rep.corr = 1;  # correct non-response
                    else:
                       key_resp_blok4_rep.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_14 (TrialHandler)
                trials_14.addData('key_resp_blok4_rep.keys',key_resp_blok4_rep.keys)
                trials_14.addData('key_resp_blok4_rep.corr', key_resp_blok4_rep.corr)
                if key_resp_blok4_rep.keys != None:  # we had a response
                    trials_14.addData('key_resp_blok4_rep.rt', key_resp_blok4_rep.rt)
                    trials_14.addData('key_resp_blok4_rep.duration', key_resp_blok4_rep.duration)
                # Run 'End Routine' code from code_16
                if key_resp_blok4_rep.corr == 1:
                    rep_fdb2 = 0
                    trials_14.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok4_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_13 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_13')
                thisExp.addLoop(trials_13)  # add the loop to the experiment
                thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
                if thisTrial_13 != None:
                    for paramName in thisTrial_13:
                        globals()[paramName] = thisTrial_13[paramName]
                
                for thisTrial_13 in trials_13:
                    currentLoop = trials_13
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
                    if thisTrial_13 != None:
                        for paramName in thisTrial_13:
                            globals()[paramName] = thisTrial_13[paramName]
                    
                    # --- Prepare to start Routine "blok4_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok4_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_17
                    if key_resp_blok4_rep.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_4.setText(fdb2)
                    # keep track of which components have finished
                    blok4_rep_feedbackComponents = [text_rep_feed_4]
                    for thisComponent in blok4_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok4_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_4* updates
                        
                        # if text_rep_feed_4 is starting this frame...
                        if text_rep_feed_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_4.frameNStart = frameN  # exact frame index
                            text_rep_feed_4.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_4.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_4, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_4.started')
                            # update status
                            text_rep_feed_4.status = STARTED
                            text_rep_feed_4.setAutoDraw(True)
                        
                        # if text_rep_feed_4 is active this frame...
                        if text_rep_feed_4.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_4 is stopping this frame...
                        if text_rep_feed_4.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_4.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_4.tStop = t  # not accounting for scr refresh
                                text_rep_feed_4.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_4.stopped')
                                # update status
                                text_rep_feed_4.status = FINISHED
                                text_rep_feed_4.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok4_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok4_rep_feedback" ---
                    for thisComponent in blok4_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok4_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_13'
                
                # get names of stimulus parameters
                if trials_13.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_13.trialList[0].keys()
                # save data for this loop
                trials_13.saveAsText(filename + 'trials_13.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_14'
            
            # get names of stimulus parameters
            if trials_14.trialList in ([], [None], None):
                params = []
            else:
                params = trials_14.trialList[0].keys()
            # save data for this loop
            trials_14.saveAsText(filename + 'trials_14.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_block4'
        
        # get names of stimulus parameters
        if loop_block4.trialList in ([], [None], None):
            params = []
        else:
            params = loop_block4.trialList[0].keys()
        # save data for this loop
        loop_block4.saveAsText(filename + 'loop_block4.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok_5_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok_5_inst.started', globalClock.getTime())
        key_resp_blok5_inst.keys = []
        key_resp_blok5_inst.rt = []
        _key_resp_blok5_inst_allKeys = []
        # keep track of which components have finished
        blok_5_instComponents = [text_blok5_ins, key_resp_blok5_inst]
        for thisComponent in blok_5_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok_5_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok5_ins* updates
            
            # if text_blok5_ins is starting this frame...
            if text_blok5_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok5_ins.frameNStart = frameN  # exact frame index
                text_blok5_ins.tStart = t  # local t and not account for scr refresh
                text_blok5_ins.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok5_ins, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok5_ins.started')
                # update status
                text_blok5_ins.status = STARTED
                text_blok5_ins.setAutoDraw(True)
            
            # if text_blok5_ins is active this frame...
            if text_blok5_ins.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok5_inst* updates
            waitOnFlip = False
            
            # if key_resp_blok5_inst is starting this frame...
            if key_resp_blok5_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok5_inst.frameNStart = frameN  # exact frame index
                key_resp_blok5_inst.tStart = t  # local t and not account for scr refresh
                key_resp_blok5_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok5_inst, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok5_inst.started')
                # update status
                key_resp_blok5_inst.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok5_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok5_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok5_inst.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok5_inst.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok5_inst_allKeys.extend(theseKeys)
                if len(_key_resp_blok5_inst_allKeys):
                    key_resp_blok5_inst.keys = _key_resp_blok5_inst_allKeys[-1].name  # just the last key pressed
                    key_resp_blok5_inst.rt = _key_resp_blok5_inst_allKeys[-1].rt
                    key_resp_blok5_inst.duration = _key_resp_blok5_inst_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok_5_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok_5_inst" ---
        for thisComponent in blok_5_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok_5_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok5_inst.keys in ['', [], None]:  # No response was made
            key_resp_blok5_inst.keys = None
        condition1.addData('key_resp_blok5_inst.keys',key_resp_blok5_inst.keys)
        if key_resp_blok5_inst.keys != None:  # we had a response
            condition1.addData('key_resp_blok5_inst.rt', key_resp_blok5_inst.rt)
            condition1.addData('key_resp_blok5_inst.duration', key_resp_blok5_inst.duration)
        # the Routine "blok_5_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_blok5 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block5Condition1.xlsx'),
            seed=None, name='loop_blok5')
        thisExp.addLoop(loop_blok5)  # add the loop to the experiment
        thisLoop_blok5 = loop_blok5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok5.rgb)
        if thisLoop_blok5 != None:
            for paramName in thisLoop_blok5:
                globals()[paramName] = thisLoop_blok5[paramName]
        
        for thisLoop_blok5 in loop_blok5:
            currentLoop = loop_blok5
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok5.rgb)
            if thisLoop_blok5 != None:
                for paramName in thisLoop_blok5:
                    globals()[paramName] = thisLoop_blok5[paramName]
            
            # --- Prepare to start Routine "blok5_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok5_main.started', globalClock.getTime())
            target_image_blok5.setImage(ImageFiles)
            key_resp_blok5_main.keys = []
            key_resp_blok5_main.rt = []
            _key_resp_blok5_main_allKeys = []
            # keep track of which components have finished
            blok5_mainComponents = [target_image_blok5, key_resp_blok5_main, text_coveredattr_main_5, text_uncoveredunattr_main_5]
            for thisComponent in blok5_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok5_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok5* updates
                
                # if target_image_blok5 is starting this frame...
                if target_image_blok5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok5.frameNStart = frameN  # exact frame index
                    target_image_blok5.tStart = t  # local t and not account for scr refresh
                    target_image_blok5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok5.started')
                    # update status
                    target_image_blok5.status = STARTED
                    target_image_blok5.setAutoDraw(True)
                
                # if target_image_blok5 is active this frame...
                if target_image_blok5.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok5_main* updates
                waitOnFlip = False
                
                # if key_resp_blok5_main is starting this frame...
                if key_resp_blok5_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok5_main.frameNStart = frameN  # exact frame index
                    key_resp_blok5_main.tStart = t  # local t and not account for scr refresh
                    key_resp_blok5_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok5_main, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok5_main.started')
                    # update status
                    key_resp_blok5_main.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok5_main.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok5_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok5_main.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok5_main.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok5_main_allKeys.extend(theseKeys)
                    if len(_key_resp_blok5_main_allKeys):
                        key_resp_blok5_main.keys = _key_resp_blok5_main_allKeys[-1].name  # just the last key pressed
                        key_resp_blok5_main.rt = _key_resp_blok5_main_allKeys[-1].rt
                        key_resp_blok5_main.duration = _key_resp_blok5_main_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok5_main.keys == str(corrAns)) or (key_resp_blok5_main.keys == corrAns):
                            key_resp_blok5_main.corr = 1
                        else:
                            key_resp_blok5_main.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_coveredattr_main_5* updates
                
                # if text_coveredattr_main_5 is starting this frame...
                if text_coveredattr_main_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_coveredattr_main_5.frameNStart = frameN  # exact frame index
                    text_coveredattr_main_5.tStart = t  # local t and not account for scr refresh
                    text_coveredattr_main_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_coveredattr_main_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_coveredattr_main_5.started')
                    # update status
                    text_coveredattr_main_5.status = STARTED
                    text_coveredattr_main_5.setAutoDraw(True)
                
                # if text_coveredattr_main_5 is active this frame...
                if text_coveredattr_main_5.status == STARTED:
                    # update params
                    pass
                
                # *text_uncoveredunattr_main_5* updates
                
                # if text_uncoveredunattr_main_5 is starting this frame...
                if text_uncoveredunattr_main_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncoveredunattr_main_5.frameNStart = frameN  # exact frame index
                    text_uncoveredunattr_main_5.tStart = t  # local t and not account for scr refresh
                    text_uncoveredunattr_main_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncoveredunattr_main_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncoveredunattr_main_5.started')
                    # update status
                    text_uncoveredunattr_main_5.status = STARTED
                    text_uncoveredunattr_main_5.setAutoDraw(True)
                
                # if text_uncoveredunattr_main_5 is active this frame...
                if text_uncoveredunattr_main_5.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok5_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok5_main" ---
            for thisComponent in blok5_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok5_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok5_main.keys in ['', [], None]:  # No response was made
                key_resp_blok5_main.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok5_main.corr = 1;  # correct non-response
                else:
                   key_resp_blok5_main.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_blok5 (TrialHandler)
            loop_blok5.addData('key_resp_blok5_main.keys',key_resp_blok5_main.keys)
            loop_blok5.addData('key_resp_blok5_main.corr', key_resp_blok5_main.corr)
            if key_resp_blok5_main.keys != None:  # we had a response
                loop_blok5.addData('key_resp_blok5_main.rt', key_resp_blok5_main.rt)
                loop_blok5.addData('key_resp_blok5_main.duration', key_resp_blok5_main.duration)
            # Run 'End Routine' code from code_18
            if key_resp_blok5_main.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok5_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_10 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_10')
            thisExp.addLoop(trials_10)  # add the loop to the experiment
            thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
            if thisTrial_10 != None:
                for paramName in thisTrial_10:
                    globals()[paramName] = thisTrial_10[paramName]
            
            for thisTrial_10 in trials_10:
                currentLoop = trials_10
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
                if thisTrial_10 != None:
                    for paramName in thisTrial_10:
                        globals()[paramName] = thisTrial_10[paramName]
                
                # --- Prepare to start Routine "blok5_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok5_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_19
                if key_resp_blok5_main.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_6.setText(fdb)
                # keep track of which components have finished
                blok5_main_feedbackComponents = [text_fdb_6]
                for thisComponent in blok5_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok5_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_6* updates
                    
                    # if text_fdb_6 is starting this frame...
                    if text_fdb_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_6.frameNStart = frameN  # exact frame index
                        text_fdb_6.tStart = t  # local t and not account for scr refresh
                        text_fdb_6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_6.started')
                        # update status
                        text_fdb_6.status = STARTED
                        text_fdb_6.setAutoDraw(True)
                    
                    # if text_fdb_6 is active this frame...
                    if text_fdb_6.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_6 is stopping this frame...
                    if text_fdb_6.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_6.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_6.tStop = t  # not accounting for scr refresh
                            text_fdb_6.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_6.stopped')
                            # update status
                            text_fdb_6.status = FINISHED
                            text_fdb_6.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok5_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok5_main_feedback" ---
                for thisComponent in blok5_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok5_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_10'
            
            # get names of stimulus parameters
            if trials_10.trialList in ([], [None], None):
                params = []
            else:
                params = trials_10.trialList[0].keys()
            # save data for this loop
            trials_10.saveAsText(filename + 'trials_10.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_12 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_12')
            thisExp.addLoop(trials_12)  # add the loop to the experiment
            thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
            if thisTrial_12 != None:
                for paramName in thisTrial_12:
                    globals()[paramName] = thisTrial_12[paramName]
            
            for thisTrial_12 in trials_12:
                currentLoop = trials_12
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
                if thisTrial_12 != None:
                    for paramName in thisTrial_12:
                        globals()[paramName] = thisTrial_12[paramName]
                
                # --- Prepare to start Routine "blok5_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok5_rep.started', globalClock.getTime())
                target_image_blok5_rep.setImage(ImageFiles)
                key_resp_blok5_rep.keys = []
                key_resp_blok5_rep.rt = []
                _key_resp_blok5_rep_allKeys = []
                # keep track of which components have finished
                blok5_repComponents = [target_image_blok5_rep, key_resp_blok5_rep, text_coveredattr_rep, text_uncoveredunattr_rep]
                for thisComponent in blok5_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok5_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *target_image_blok5_rep* updates
                    
                    # if target_image_blok5_rep is starting this frame...
                    if target_image_blok5_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        target_image_blok5_rep.frameNStart = frameN  # exact frame index
                        target_image_blok5_rep.tStart = t  # local t and not account for scr refresh
                        target_image_blok5_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_image_blok5_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_image_blok5_rep.started')
                        # update status
                        target_image_blok5_rep.status = STARTED
                        target_image_blok5_rep.setAutoDraw(True)
                    
                    # if target_image_blok5_rep is active this frame...
                    if target_image_blok5_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok5_rep* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok5_rep is starting this frame...
                    if key_resp_blok5_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok5_rep.frameNStart = frameN  # exact frame index
                        key_resp_blok5_rep.tStart = t  # local t and not account for scr refresh
                        key_resp_blok5_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok5_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok5_rep.started')
                        # update status
                        key_resp_blok5_rep.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok5_rep.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok5_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok5_rep.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok5_rep.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok5_rep_allKeys.extend(theseKeys)
                        if len(_key_resp_blok5_rep_allKeys):
                            key_resp_blok5_rep.keys = _key_resp_blok5_rep_allKeys[-1].name  # just the last key pressed
                            key_resp_blok5_rep.rt = _key_resp_blok5_rep_allKeys[-1].rt
                            key_resp_blok5_rep.duration = _key_resp_blok5_rep_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok5_rep.keys == str(corrAns)) or (key_resp_blok5_rep.keys == corrAns):
                                key_resp_blok5_rep.corr = 1
                            else:
                                key_resp_blok5_rep.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_coveredattr_rep* updates
                    
                    # if text_coveredattr_rep is starting this frame...
                    if text_coveredattr_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_coveredattr_rep.frameNStart = frameN  # exact frame index
                        text_coveredattr_rep.tStart = t  # local t and not account for scr refresh
                        text_coveredattr_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_coveredattr_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_coveredattr_rep.started')
                        # update status
                        text_coveredattr_rep.status = STARTED
                        text_coveredattr_rep.setAutoDraw(True)
                    
                    # if text_coveredattr_rep is active this frame...
                    if text_coveredattr_rep.status == STARTED:
                        # update params
                        pass
                    
                    # *text_uncoveredunattr_rep* updates
                    
                    # if text_uncoveredunattr_rep is starting this frame...
                    if text_uncoveredunattr_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncoveredunattr_rep.frameNStart = frameN  # exact frame index
                        text_uncoveredunattr_rep.tStart = t  # local t and not account for scr refresh
                        text_uncoveredunattr_rep.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncoveredunattr_rep, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncoveredunattr_rep.started')
                        # update status
                        text_uncoveredunattr_rep.status = STARTED
                        text_uncoveredunattr_rep.setAutoDraw(True)
                    
                    # if text_uncoveredunattr_rep is active this frame...
                    if text_uncoveredunattr_rep.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok5_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok5_rep" ---
                for thisComponent in blok5_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok5_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok5_rep.keys in ['', [], None]:  # No response was made
                    key_resp_blok5_rep.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok5_rep.corr = 1;  # correct non-response
                    else:
                       key_resp_blok5_rep.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_12 (TrialHandler)
                trials_12.addData('key_resp_blok5_rep.keys',key_resp_blok5_rep.keys)
                trials_12.addData('key_resp_blok5_rep.corr', key_resp_blok5_rep.corr)
                if key_resp_blok5_rep.keys != None:  # we had a response
                    trials_12.addData('key_resp_blok5_rep.rt', key_resp_blok5_rep.rt)
                    trials_12.addData('key_resp_blok5_rep.duration', key_resp_blok5_rep.duration)
                # Run 'End Routine' code from code_20
                if key_resp_blok5_rep.corr == 1:
                    rep_fdb2 = 0
                    trials_12.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok5_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_15 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_15')
                thisExp.addLoop(trials_15)  # add the loop to the experiment
                thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
                if thisTrial_15 != None:
                    for paramName in thisTrial_15:
                        globals()[paramName] = thisTrial_15[paramName]
                
                for thisTrial_15 in trials_15:
                    currentLoop = trials_15
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
                    if thisTrial_15 != None:
                        for paramName in thisTrial_15:
                            globals()[paramName] = thisTrial_15[paramName]
                    
                    # --- Prepare to start Routine "blok5_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok5_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_21
                    if key_resp_blok5_rep.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_5.setText(fdb2)
                    # keep track of which components have finished
                    blok5_rep_feedbackComponents = [text_rep_feed_5]
                    for thisComponent in blok5_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok5_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_5* updates
                        
                        # if text_rep_feed_5 is starting this frame...
                        if text_rep_feed_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_5.frameNStart = frameN  # exact frame index
                            text_rep_feed_5.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_5.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_5, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_5.started')
                            # update status
                            text_rep_feed_5.status = STARTED
                            text_rep_feed_5.setAutoDraw(True)
                        
                        # if text_rep_feed_5 is active this frame...
                        if text_rep_feed_5.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_5 is stopping this frame...
                        if text_rep_feed_5.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_5.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_5.tStop = t  # not accounting for scr refresh
                                text_rep_feed_5.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_5.stopped')
                                # update status
                                text_rep_feed_5.status = FINISHED
                                text_rep_feed_5.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok5_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok5_rep_feedback" ---
                    for thisComponent in blok5_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok5_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_15'
                
                # get names of stimulus parameters
                if trials_15.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_15.trialList[0].keys()
                # save data for this loop
                trials_15.saveAsText(filename + 'trials_15.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_12'
            
            # get names of stimulus parameters
            if trials_12.trialList in ([], [None], None):
                params = []
            else:
                params = trials_12.trialList[0].keys()
            # save data for this loop
            trials_12.saveAsText(filename + 'trials_12.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_blok5'
        
        # get names of stimulus parameters
        if loop_blok5.trialList in ([], [None], None):
            params = []
        else:
            params = loop_blok5.trialList[0].keys()
        # save data for this loop
        loop_blok5.saveAsText(filename + 'loop_blok5.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "thanks_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('thanks_1.started', globalClock.getTime())
        key_resp_thanks1.keys = []
        key_resp_thanks1.rt = []
        _key_resp_thanks1_allKeys = []
        # keep track of which components have finished
        thanks_1Components = [text_thanks1, key_resp_thanks1]
        for thisComponent in thanks_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "thanks_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_thanks1* updates
            
            # if text_thanks1 is starting this frame...
            if text_thanks1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_thanks1.frameNStart = frameN  # exact frame index
                text_thanks1.tStart = t  # local t and not account for scr refresh
                text_thanks1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_thanks1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_thanks1.started')
                # update status
                text_thanks1.status = STARTED
                text_thanks1.setAutoDraw(True)
            
            # if text_thanks1 is active this frame...
            if text_thanks1.status == STARTED:
                # update params
                pass
            
            # *key_resp_thanks1* updates
            waitOnFlip = False
            
            # if key_resp_thanks1 is starting this frame...
            if key_resp_thanks1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_thanks1.frameNStart = frameN  # exact frame index
                key_resp_thanks1.tStart = t  # local t and not account for scr refresh
                key_resp_thanks1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_thanks1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_thanks1.started')
                # update status
                key_resp_thanks1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_thanks1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_thanks1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_thanks1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_thanks1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_thanks1_allKeys.extend(theseKeys)
                if len(_key_resp_thanks1_allKeys):
                    key_resp_thanks1.keys = _key_resp_thanks1_allKeys[-1].name  # just the last key pressed
                    key_resp_thanks1.rt = _key_resp_thanks1_allKeys[-1].rt
                    key_resp_thanks1.duration = _key_resp_thanks1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in thanks_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "thanks_1" ---
        for thisComponent in thanks_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('thanks_1.stopped', globalClock.getTime())
        # check responses
        if key_resp_thanks1.keys in ['', [], None]:  # No response was made
            key_resp_thanks1.keys = None
        condition1.addData('key_resp_thanks1.keys',key_resp_thanks1.keys)
        if key_resp_thanks1.keys != None:  # we had a response
            condition1.addData('key_resp_thanks1.rt', key_resp_thanks1.rt)
            condition1.addData('key_resp_thanks1.duration', key_resp_thanks1.duration)
        # the Routine "thanks_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "exitcode1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('exitcode1.started', globalClock.getTime())
        # keep track of which components have finished
        exitcode1Components = []
        for thisComponent in exitcode1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exitcode1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from exitcode
            print("Experiment has ended")
            core.quit()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exitcode1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exitcode1" ---
        for thisComponent in exitcode1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('exitcode1.stopped', globalClock.getTime())
        # the Routine "exitcode1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed nRepsA repeats of 'condition1'
    
    # get names of stimulus parameters
    if condition1.trialList in ([], [None], None):
        params = []
    else:
        params = condition1.trialList[0].keys()
    # save data for this loop
    condition1.saveAsText(filename + 'condition1.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    condition2 = data.TrialHandler(nReps=nRepsB, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='condition2')
    thisExp.addLoop(condition2)  # add the loop to the experiment
    thisCondition2 = condition2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
    if thisCondition2 != None:
        for paramName in thisCondition2:
            globals()[paramName] = thisCondition2[paramName]
    
    for thisCondition2 in condition2:
        currentLoop = condition2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
        if thisCondition2 != None:
            for paramName in thisCondition2:
                globals()[paramName] = thisCondition2[paramName]
        
        # --- Prepare to start Routine "blok4_2ins" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok4_2ins.started', globalClock.getTime())
        key_resp_blok4_inst_2.keys = []
        key_resp_blok4_inst_2.rt = []
        _key_resp_blok4_inst_2_allKeys = []
        # keep track of which components have finished
        blok4_2insComponents = [text_blok4_ins_2, key_resp_blok4_inst_2]
        for thisComponent in blok4_2insComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok4_2ins" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok4_ins_2* updates
            
            # if text_blok4_ins_2 is starting this frame...
            if text_blok4_ins_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok4_ins_2.frameNStart = frameN  # exact frame index
                text_blok4_ins_2.tStart = t  # local t and not account for scr refresh
                text_blok4_ins_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok4_ins_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok4_ins_2.started')
                # update status
                text_blok4_ins_2.status = STARTED
                text_blok4_ins_2.setAutoDraw(True)
            
            # if text_blok4_ins_2 is active this frame...
            if text_blok4_ins_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok4_inst_2* updates
            waitOnFlip = False
            
            # if key_resp_blok4_inst_2 is starting this frame...
            if key_resp_blok4_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok4_inst_2.frameNStart = frameN  # exact frame index
                key_resp_blok4_inst_2.tStart = t  # local t and not account for scr refresh
                key_resp_blok4_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok4_inst_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok4_inst_2.started')
                # update status
                key_resp_blok4_inst_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok4_inst_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok4_inst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok4_inst_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok4_inst_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok4_inst_2_allKeys.extend(theseKeys)
                if len(_key_resp_blok4_inst_2_allKeys):
                    key_resp_blok4_inst_2.keys = _key_resp_blok4_inst_2_allKeys[-1].name  # just the last key pressed
                    key_resp_blok4_inst_2.rt = _key_resp_blok4_inst_2_allKeys[-1].rt
                    key_resp_blok4_inst_2.duration = _key_resp_blok4_inst_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok4_2insComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok4_2ins" ---
        for thisComponent in blok4_2insComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok4_2ins.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok4_inst_2.keys in ['', [], None]:  # No response was made
            key_resp_blok4_inst_2.keys = None
        condition2.addData('key_resp_blok4_inst_2.keys',key_resp_blok4_inst_2.keys)
        if key_resp_blok4_inst_2.keys != None:  # we had a response
            condition2.addData('key_resp_blok4_inst_2.rt', key_resp_blok4_inst_2.rt)
            condition2.addData('key_resp_blok4_inst_2.duration', key_resp_blok4_inst_2.duration)
        # the Routine "blok4_2ins" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_blok4_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block4Condition1.xlsx'),
            seed=None, name='loop_blok4_2')
        thisExp.addLoop(loop_blok4_2)  # add the loop to the experiment
        thisLoop_blok4_2 = loop_blok4_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok4_2.rgb)
        if thisLoop_blok4_2 != None:
            for paramName in thisLoop_blok4_2:
                globals()[paramName] = thisLoop_blok4_2[paramName]
        
        for thisLoop_blok4_2 in loop_blok4_2:
            currentLoop = loop_blok4_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok4_2.rgb)
            if thisLoop_blok4_2 != None:
                for paramName in thisLoop_blok4_2:
                    globals()[paramName] = thisLoop_blok4_2[paramName]
            
            # --- Prepare to start Routine "blok4_main_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok4_main_2.started', globalClock.getTime())
            target_image_blok4_2.setImage(ImageFiles)
            key_resp_blok4_main_2.keys = []
            key_resp_blok4_main_2.rt = []
            _key_resp_blok4_main_2_allKeys = []
            # keep track of which components have finished
            blok4_main_2Components = [target_image_blok4_2, key_resp_blok4_main_2, text_covered_main_4_2, text_uncovered_main_4_2]
            for thisComponent in blok4_main_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok4_main_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok4_2* updates
                
                # if target_image_blok4_2 is starting this frame...
                if target_image_blok4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok4_2.frameNStart = frameN  # exact frame index
                    target_image_blok4_2.tStart = t  # local t and not account for scr refresh
                    target_image_blok4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok4_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok4_2.started')
                    # update status
                    target_image_blok4_2.status = STARTED
                    target_image_blok4_2.setAutoDraw(True)
                
                # if target_image_blok4_2 is active this frame...
                if target_image_blok4_2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok4_main_2* updates
                waitOnFlip = False
                
                # if key_resp_blok4_main_2 is starting this frame...
                if key_resp_blok4_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok4_main_2.frameNStart = frameN  # exact frame index
                    key_resp_blok4_main_2.tStart = t  # local t and not account for scr refresh
                    key_resp_blok4_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok4_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok4_main_2.started')
                    # update status
                    key_resp_blok4_main_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok4_main_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok4_main_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok4_main_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok4_main_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok4_main_2_allKeys.extend(theseKeys)
                    if len(_key_resp_blok4_main_2_allKeys):
                        key_resp_blok4_main_2.keys = _key_resp_blok4_main_2_allKeys[-1].name  # just the last key pressed
                        key_resp_blok4_main_2.rt = _key_resp_blok4_main_2_allKeys[-1].rt
                        key_resp_blok4_main_2.duration = _key_resp_blok4_main_2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok4_main_2.keys == str(corrAns)) or (key_resp_blok4_main_2.keys == corrAns):
                            key_resp_blok4_main_2.corr = 1
                        else:
                            key_resp_blok4_main_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_covered_main_4_2* updates
                
                # if text_covered_main_4_2 is starting this frame...
                if text_covered_main_4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_covered_main_4_2.frameNStart = frameN  # exact frame index
                    text_covered_main_4_2.tStart = t  # local t and not account for scr refresh
                    text_covered_main_4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_covered_main_4_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_covered_main_4_2.started')
                    # update status
                    text_covered_main_4_2.status = STARTED
                    text_covered_main_4_2.setAutoDraw(True)
                
                # if text_covered_main_4_2 is active this frame...
                if text_covered_main_4_2.status == STARTED:
                    # update params
                    pass
                
                # *text_uncovered_main_4_2* updates
                
                # if text_uncovered_main_4_2 is starting this frame...
                if text_uncovered_main_4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncovered_main_4_2.frameNStart = frameN  # exact frame index
                    text_uncovered_main_4_2.tStart = t  # local t and not account for scr refresh
                    text_uncovered_main_4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncovered_main_4_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncovered_main_4_2.started')
                    # update status
                    text_uncovered_main_4_2.status = STARTED
                    text_uncovered_main_4_2.setAutoDraw(True)
                
                # if text_uncovered_main_4_2 is active this frame...
                if text_uncovered_main_4_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok4_main_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok4_main_2" ---
            for thisComponent in blok4_main_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok4_main_2.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok4_main_2.keys in ['', [], None]:  # No response was made
                key_resp_blok4_main_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok4_main_2.corr = 1;  # correct non-response
                else:
                   key_resp_blok4_main_2.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_blok4_2 (TrialHandler)
            loop_blok4_2.addData('key_resp_blok4_main_2.keys',key_resp_blok4_main_2.keys)
            loop_blok4_2.addData('key_resp_blok4_main_2.corr', key_resp_blok4_main_2.corr)
            if key_resp_blok4_main_2.keys != None:  # we had a response
                loop_blok4_2.addData('key_resp_blok4_main_2.rt', key_resp_blok4_main_2.rt)
                loop_blok4_2.addData('key_resp_blok4_main_2.duration', key_resp_blok4_main_2.duration)
            # Run 'End Routine' code from code_22
            if key_resp_blok4_main_2.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok4_main_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_16 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_16')
            thisExp.addLoop(trials_16)  # add the loop to the experiment
            thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
            if thisTrial_16 != None:
                for paramName in thisTrial_16:
                    globals()[paramName] = thisTrial_16[paramName]
            
            for thisTrial_16 in trials_16:
                currentLoop = trials_16
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
                if thisTrial_16 != None:
                    for paramName in thisTrial_16:
                        globals()[paramName] = thisTrial_16[paramName]
                
                # --- Prepare to start Routine "blok4_main_2_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok4_main_2_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_23
                if key_resp_blok4_main_2.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_7.setText(fdb)
                # keep track of which components have finished
                blok4_main_2_feedbackComponents = [text_fdb_7]
                for thisComponent in blok4_main_2_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok4_main_2_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_7* updates
                    
                    # if text_fdb_7 is starting this frame...
                    if text_fdb_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_7.frameNStart = frameN  # exact frame index
                        text_fdb_7.tStart = t  # local t and not account for scr refresh
                        text_fdb_7.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_7, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_7.started')
                        # update status
                        text_fdb_7.status = STARTED
                        text_fdb_7.setAutoDraw(True)
                    
                    # if text_fdb_7 is active this frame...
                    if text_fdb_7.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_7 is stopping this frame...
                    if text_fdb_7.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_7.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_7.tStop = t  # not accounting for scr refresh
                            text_fdb_7.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_7.stopped')
                            # update status
                            text_fdb_7.status = FINISHED
                            text_fdb_7.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok4_main_2_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok4_main_2_feedback" ---
                for thisComponent in blok4_main_2_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok4_main_2_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_16'
            
            # get names of stimulus parameters
            if trials_16.trialList in ([], [None], None):
                params = []
            else:
                params = trials_16.trialList[0].keys()
            # save data for this loop
            trials_16.saveAsText(filename + 'trials_16.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_18 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_18')
            thisExp.addLoop(trials_18)  # add the loop to the experiment
            thisTrial_18 = trials_18.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
            if thisTrial_18 != None:
                for paramName in thisTrial_18:
                    globals()[paramName] = thisTrial_18[paramName]
            
            for thisTrial_18 in trials_18:
                currentLoop = trials_18
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
                if thisTrial_18 != None:
                    for paramName in thisTrial_18:
                        globals()[paramName] = thisTrial_18[paramName]
                
                # --- Prepare to start Routine "blok4_2_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok4_2_rep.started', globalClock.getTime())
                target_image_blok4_rep_2.setImage(ImageFiles)
                key_resp_blok4_rep_2.keys = []
                key_resp_blok4_rep_2.rt = []
                _key_resp_blok4_rep_2_allKeys = []
                # keep track of which components have finished
                blok4_2_repComponents = [target_image_blok4_rep_2, key_resp_blok4_rep_2, text_covered_rep_2, text_uncovered_rep_2]
                for thisComponent in blok4_2_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok4_2_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *target_image_blok4_rep_2* updates
                    
                    # if target_image_blok4_rep_2 is starting this frame...
                    if target_image_blok4_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        target_image_blok4_rep_2.frameNStart = frameN  # exact frame index
                        target_image_blok4_rep_2.tStart = t  # local t and not account for scr refresh
                        target_image_blok4_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_image_blok4_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_image_blok4_rep_2.started')
                        # update status
                        target_image_blok4_rep_2.status = STARTED
                        target_image_blok4_rep_2.setAutoDraw(True)
                    
                    # if target_image_blok4_rep_2 is active this frame...
                    if target_image_blok4_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok4_rep_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok4_rep_2 is starting this frame...
                    if key_resp_blok4_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok4_rep_2.frameNStart = frameN  # exact frame index
                        key_resp_blok4_rep_2.tStart = t  # local t and not account for scr refresh
                        key_resp_blok4_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok4_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok4_rep_2.started')
                        # update status
                        key_resp_blok4_rep_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok4_rep_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok4_rep_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok4_rep_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok4_rep_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok4_rep_2_allKeys.extend(theseKeys)
                        if len(_key_resp_blok4_rep_2_allKeys):
                            key_resp_blok4_rep_2.keys = _key_resp_blok4_rep_2_allKeys[-1].name  # just the last key pressed
                            key_resp_blok4_rep_2.rt = _key_resp_blok4_rep_2_allKeys[-1].rt
                            key_resp_blok4_rep_2.duration = _key_resp_blok4_rep_2_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok4_rep_2.keys == str(corrAns)) or (key_resp_blok4_rep_2.keys == corrAns):
                                key_resp_blok4_rep_2.corr = 1
                            else:
                                key_resp_blok4_rep_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_covered_rep_2* updates
                    
                    # if text_covered_rep_2 is starting this frame...
                    if text_covered_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_covered_rep_2.frameNStart = frameN  # exact frame index
                        text_covered_rep_2.tStart = t  # local t and not account for scr refresh
                        text_covered_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_covered_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_covered_rep_2.started')
                        # update status
                        text_covered_rep_2.status = STARTED
                        text_covered_rep_2.setAutoDraw(True)
                    
                    # if text_covered_rep_2 is active this frame...
                    if text_covered_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *text_uncovered_rep_2* updates
                    
                    # if text_uncovered_rep_2 is starting this frame...
                    if text_uncovered_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncovered_rep_2.frameNStart = frameN  # exact frame index
                        text_uncovered_rep_2.tStart = t  # local t and not account for scr refresh
                        text_uncovered_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncovered_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncovered_rep_2.started')
                        # update status
                        text_uncovered_rep_2.status = STARTED
                        text_uncovered_rep_2.setAutoDraw(True)
                    
                    # if text_uncovered_rep_2 is active this frame...
                    if text_uncovered_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok4_2_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok4_2_rep" ---
                for thisComponent in blok4_2_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok4_2_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok4_rep_2.keys in ['', [], None]:  # No response was made
                    key_resp_blok4_rep_2.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok4_rep_2.corr = 1;  # correct non-response
                    else:
                       key_resp_blok4_rep_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_18 (TrialHandler)
                trials_18.addData('key_resp_blok4_rep_2.keys',key_resp_blok4_rep_2.keys)
                trials_18.addData('key_resp_blok4_rep_2.corr', key_resp_blok4_rep_2.corr)
                if key_resp_blok4_rep_2.keys != None:  # we had a response
                    trials_18.addData('key_resp_blok4_rep_2.rt', key_resp_blok4_rep_2.rt)
                    trials_18.addData('key_resp_blok4_rep_2.duration', key_resp_blok4_rep_2.duration)
                # Run 'End Routine' code from code_24
                if key_resp_blok4_rep_2.corr == 1:
                    rep_fdb2 = 0
                    trials_18.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok4_2_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_17 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_17')
                thisExp.addLoop(trials_17)  # add the loop to the experiment
                thisTrial_17 = trials_17.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
                if thisTrial_17 != None:
                    for paramName in thisTrial_17:
                        globals()[paramName] = thisTrial_17[paramName]
                
                for thisTrial_17 in trials_17:
                    currentLoop = trials_17
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
                    if thisTrial_17 != None:
                        for paramName in thisTrial_17:
                            globals()[paramName] = thisTrial_17[paramName]
                    
                    # --- Prepare to start Routine "blok4_2_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok4_2_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_25
                    if key_resp_blok4_rep_2.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_4_2.setText(fdb2)
                    # keep track of which components have finished
                    blok4_2_rep_feedbackComponents = [text_rep_feed_4_2]
                    for thisComponent in blok4_2_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok4_2_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_4_2* updates
                        
                        # if text_rep_feed_4_2 is starting this frame...
                        if text_rep_feed_4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_4_2.frameNStart = frameN  # exact frame index
                            text_rep_feed_4_2.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_4_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_4_2, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_4_2.started')
                            # update status
                            text_rep_feed_4_2.status = STARTED
                            text_rep_feed_4_2.setAutoDraw(True)
                        
                        # if text_rep_feed_4_2 is active this frame...
                        if text_rep_feed_4_2.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_4_2 is stopping this frame...
                        if text_rep_feed_4_2.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_4_2.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_4_2.tStop = t  # not accounting for scr refresh
                                text_rep_feed_4_2.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_4_2.stopped')
                                # update status
                                text_rep_feed_4_2.status = FINISHED
                                text_rep_feed_4_2.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok4_2_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok4_2_rep_feedback" ---
                    for thisComponent in blok4_2_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok4_2_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_17'
                
                # get names of stimulus parameters
                if trials_17.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_17.trialList[0].keys()
                # save data for this loop
                trials_17.saveAsText(filename + 'trials_17.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_18'
            
            # get names of stimulus parameters
            if trials_18.trialList in ([], [None], None):
                params = []
            else:
                params = trials_18.trialList[0].keys()
            # save data for this loop
            trials_18.saveAsText(filename + 'trials_18.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_blok4_2'
        
        # get names of stimulus parameters
        if loop_blok4_2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_blok4_2.trialList[0].keys()
        # save data for this loop
        loop_blok4_2.saveAsText(filename + 'loop_blok4_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok2_2intr" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok2_2intr.started', globalClock.getTime())
        key_resp_blok2_inst_2.keys = []
        key_resp_blok2_inst_2.rt = []
        _key_resp_blok2_inst_2_allKeys = []
        # keep track of which components have finished
        blok2_2intrComponents = [text_blok2_inst_2, key_resp_blok2_inst_2]
        for thisComponent in blok2_2intrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok2_2intr" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok2_inst_2* updates
            
            # if text_blok2_inst_2 is starting this frame...
            if text_blok2_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok2_inst_2.frameNStart = frameN  # exact frame index
                text_blok2_inst_2.tStart = t  # local t and not account for scr refresh
                text_blok2_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok2_inst_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok2_inst_2.started')
                # update status
                text_blok2_inst_2.status = STARTED
                text_blok2_inst_2.setAutoDraw(True)
            
            # if text_blok2_inst_2 is active this frame...
            if text_blok2_inst_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok2_inst_2* updates
            waitOnFlip = False
            
            # if key_resp_blok2_inst_2 is starting this frame...
            if key_resp_blok2_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok2_inst_2.frameNStart = frameN  # exact frame index
                key_resp_blok2_inst_2.tStart = t  # local t and not account for scr refresh
                key_resp_blok2_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok2_inst_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok2_inst_2.started')
                # update status
                key_resp_blok2_inst_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok2_inst_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok2_inst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok2_inst_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok2_inst_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok2_inst_2_allKeys.extend(theseKeys)
                if len(_key_resp_blok2_inst_2_allKeys):
                    key_resp_blok2_inst_2.keys = _key_resp_blok2_inst_2_allKeys[-1].name  # just the last key pressed
                    key_resp_blok2_inst_2.rt = _key_resp_blok2_inst_2_allKeys[-1].rt
                    key_resp_blok2_inst_2.duration = _key_resp_blok2_inst_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok2_2intrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok2_2intr" ---
        for thisComponent in blok2_2intrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok2_2intr.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok2_inst_2.keys in ['', [], None]:  # No response was made
            key_resp_blok2_inst_2.keys = None
        condition2.addData('key_resp_blok2_inst_2.keys',key_resp_blok2_inst_2.keys)
        if key_resp_blok2_inst_2.keys != None:  # we had a response
            condition2.addData('key_resp_blok2_inst_2.rt', key_resp_blok2_inst_2.rt)
            condition2.addData('key_resp_blok2_inst_2.duration', key_resp_blok2_inst_2.duration)
        # the Routine "blok2_2intr" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_blok2_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block2Condition1.xlsx'),
            seed=None, name='loop_blok2_2')
        thisExp.addLoop(loop_blok2_2)  # add the loop to the experiment
        thisLoop_blok2_2 = loop_blok2_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok2_2.rgb)
        if thisLoop_blok2_2 != None:
            for paramName in thisLoop_blok2_2:
                globals()[paramName] = thisLoop_blok2_2[paramName]
        
        for thisLoop_blok2_2 in loop_blok2_2:
            currentLoop = loop_blok2_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok2_2.rgb)
            if thisLoop_blok2_2 != None:
                for paramName in thisLoop_blok2_2:
                    globals()[paramName] = thisLoop_blok2_2[paramName]
            
            # --- Prepare to start Routine "blok2_2_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok2_2_main.started', globalClock.getTime())
            image_block2_main_2.setImage(wordpic)
            key_resp_blok2_main_2.keys = []
            key_resp_blok2_main_2.rt = []
            _key_resp_blok2_main_2_allKeys = []
            # keep track of which components have finished
            blok2_2_mainComponents = [image_block2_main_2, key_resp_blok2_main_2, text_attractive_main_2, text_unattractive_main_2]
            for thisComponent in blok2_2_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok2_2_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_block2_main_2* updates
                
                # if image_block2_main_2 is starting this frame...
                if image_block2_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_block2_main_2.frameNStart = frameN  # exact frame index
                    image_block2_main_2.tStart = t  # local t and not account for scr refresh
                    image_block2_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_block2_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block2_main_2.started')
                    # update status
                    image_block2_main_2.status = STARTED
                    image_block2_main_2.setAutoDraw(True)
                
                # if image_block2_main_2 is active this frame...
                if image_block2_main_2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok2_main_2* updates
                waitOnFlip = False
                
                # if key_resp_blok2_main_2 is starting this frame...
                if key_resp_blok2_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok2_main_2.frameNStart = frameN  # exact frame index
                    key_resp_blok2_main_2.tStart = t  # local t and not account for scr refresh
                    key_resp_blok2_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok2_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok2_main_2.started')
                    # update status
                    key_resp_blok2_main_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok2_main_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok2_main_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok2_main_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok2_main_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok2_main_2_allKeys.extend(theseKeys)
                    if len(_key_resp_blok2_main_2_allKeys):
                        key_resp_blok2_main_2.keys = _key_resp_blok2_main_2_allKeys[-1].name  # just the last key pressed
                        key_resp_blok2_main_2.rt = _key_resp_blok2_main_2_allKeys[-1].rt
                        key_resp_blok2_main_2.duration = _key_resp_blok2_main_2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok2_main_2.keys == str(corrAns)) or (key_resp_blok2_main_2.keys == corrAns):
                            key_resp_blok2_main_2.corr = 1
                        else:
                            key_resp_blok2_main_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_attractive_main_2* updates
                
                # if text_attractive_main_2 is starting this frame...
                if text_attractive_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_attractive_main_2.frameNStart = frameN  # exact frame index
                    text_attractive_main_2.tStart = t  # local t and not account for scr refresh
                    text_attractive_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_attractive_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_attractive_main_2.started')
                    # update status
                    text_attractive_main_2.status = STARTED
                    text_attractive_main_2.setAutoDraw(True)
                
                # if text_attractive_main_2 is active this frame...
                if text_attractive_main_2.status == STARTED:
                    # update params
                    pass
                
                # *text_unattractive_main_2* updates
                
                # if text_unattractive_main_2 is starting this frame...
                if text_unattractive_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_unattractive_main_2.frameNStart = frameN  # exact frame index
                    text_unattractive_main_2.tStart = t  # local t and not account for scr refresh
                    text_unattractive_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_unattractive_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_unattractive_main_2.started')
                    # update status
                    text_unattractive_main_2.status = STARTED
                    text_unattractive_main_2.setAutoDraw(True)
                
                # if text_unattractive_main_2 is active this frame...
                if text_unattractive_main_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok2_2_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok2_2_main" ---
            for thisComponent in blok2_2_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok2_2_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok2_main_2.keys in ['', [], None]:  # No response was made
                key_resp_blok2_main_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok2_main_2.corr = 1;  # correct non-response
                else:
                   key_resp_blok2_main_2.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_blok2_2 (TrialHandler)
            loop_blok2_2.addData('key_resp_blok2_main_2.keys',key_resp_blok2_main_2.keys)
            loop_blok2_2.addData('key_resp_blok2_main_2.corr', key_resp_blok2_main_2.corr)
            if key_resp_blok2_main_2.keys != None:  # we had a response
                loop_blok2_2.addData('key_resp_blok2_main_2.rt', key_resp_blok2_main_2.rt)
                loop_blok2_2.addData('key_resp_blok2_main_2.duration', key_resp_blok2_main_2.duration)
            # Run 'End Routine' code from code_26
            if key_resp_blok2_main_2.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok2_2_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_19 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_19')
            thisExp.addLoop(trials_19)  # add the loop to the experiment
            thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
            if thisTrial_19 != None:
                for paramName in thisTrial_19:
                    globals()[paramName] = thisTrial_19[paramName]
            
            for thisTrial_19 in trials_19:
                currentLoop = trials_19
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
                if thisTrial_19 != None:
                    for paramName in thisTrial_19:
                        globals()[paramName] = thisTrial_19[paramName]
                
                # --- Prepare to start Routine "blok2_2_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok2_2_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_27
                if key_resp_blok2_main_2.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_8.setText(fdb)
                # keep track of which components have finished
                blok2_2_main_feedbackComponents = [text_fdb_8]
                for thisComponent in blok2_2_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok2_2_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_8* updates
                    
                    # if text_fdb_8 is starting this frame...
                    if text_fdb_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_8.frameNStart = frameN  # exact frame index
                        text_fdb_8.tStart = t  # local t and not account for scr refresh
                        text_fdb_8.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_8, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_8.started')
                        # update status
                        text_fdb_8.status = STARTED
                        text_fdb_8.setAutoDraw(True)
                    
                    # if text_fdb_8 is active this frame...
                    if text_fdb_8.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_8 is stopping this frame...
                    if text_fdb_8.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_8.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_8.tStop = t  # not accounting for scr refresh
                            text_fdb_8.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_8.stopped')
                            # update status
                            text_fdb_8.status = FINISHED
                            text_fdb_8.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok2_2_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok2_2_main_feedback" ---
                for thisComponent in blok2_2_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok2_2_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_19'
            
            # get names of stimulus parameters
            if trials_19.trialList in ([], [None], None):
                params = []
            else:
                params = trials_19.trialList[0].keys()
            # save data for this loop
            trials_19.saveAsText(filename + 'trials_19.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_21 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_21')
            thisExp.addLoop(trials_21)  # add the loop to the experiment
            thisTrial_21 = trials_21.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
            if thisTrial_21 != None:
                for paramName in thisTrial_21:
                    globals()[paramName] = thisTrial_21[paramName]
            
            for thisTrial_21 in trials_21:
                currentLoop = trials_21
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
                if thisTrial_21 != None:
                    for paramName in thisTrial_21:
                        globals()[paramName] = thisTrial_21[paramName]
                
                # --- Prepare to start Routine "blok2_2_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok2_2_rep.started', globalClock.getTime())
                image_block2_rep_2.setImage(wordpic)
                key_resp_blok2_rep_2.keys = []
                key_resp_blok2_rep_2.rt = []
                _key_resp_blok2_rep_2_allKeys = []
                # keep track of which components have finished
                blok2_2_repComponents = [image_block2_rep_2, key_resp_blok2_rep_2, text_attractive_rep_2, text_unattractive_rep_2]
                for thisComponent in blok2_2_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok2_2_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_block2_rep_2* updates
                    
                    # if image_block2_rep_2 is starting this frame...
                    if image_block2_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_block2_rep_2.frameNStart = frameN  # exact frame index
                        image_block2_rep_2.tStart = t  # local t and not account for scr refresh
                        image_block2_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_block2_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_block2_rep_2.started')
                        # update status
                        image_block2_rep_2.status = STARTED
                        image_block2_rep_2.setAutoDraw(True)
                    
                    # if image_block2_rep_2 is active this frame...
                    if image_block2_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok2_rep_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok2_rep_2 is starting this frame...
                    if key_resp_blok2_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok2_rep_2.frameNStart = frameN  # exact frame index
                        key_resp_blok2_rep_2.tStart = t  # local t and not account for scr refresh
                        key_resp_blok2_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok2_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok2_rep_2.started')
                        # update status
                        key_resp_blok2_rep_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok2_rep_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok2_rep_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok2_rep_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok2_rep_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok2_rep_2_allKeys.extend(theseKeys)
                        if len(_key_resp_blok2_rep_2_allKeys):
                            key_resp_blok2_rep_2.keys = _key_resp_blok2_rep_2_allKeys[-1].name  # just the last key pressed
                            key_resp_blok2_rep_2.rt = _key_resp_blok2_rep_2_allKeys[-1].rt
                            key_resp_blok2_rep_2.duration = _key_resp_blok2_rep_2_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok2_rep_2.keys == str(corrAns)) or (key_resp_blok2_rep_2.keys == corrAns):
                                key_resp_blok2_rep_2.corr = 1
                            else:
                                key_resp_blok2_rep_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_attractive_rep_2* updates
                    
                    # if text_attractive_rep_2 is starting this frame...
                    if text_attractive_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_attractive_rep_2.frameNStart = frameN  # exact frame index
                        text_attractive_rep_2.tStart = t  # local t and not account for scr refresh
                        text_attractive_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_attractive_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_attractive_rep_2.started')
                        # update status
                        text_attractive_rep_2.status = STARTED
                        text_attractive_rep_2.setAutoDraw(True)
                    
                    # if text_attractive_rep_2 is active this frame...
                    if text_attractive_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *text_unattractive_rep_2* updates
                    
                    # if text_unattractive_rep_2 is starting this frame...
                    if text_unattractive_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_unattractive_rep_2.frameNStart = frameN  # exact frame index
                        text_unattractive_rep_2.tStart = t  # local t and not account for scr refresh
                        text_unattractive_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_unattractive_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_unattractive_rep_2.started')
                        # update status
                        text_unattractive_rep_2.status = STARTED
                        text_unattractive_rep_2.setAutoDraw(True)
                    
                    # if text_unattractive_rep_2 is active this frame...
                    if text_unattractive_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok2_2_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok2_2_rep" ---
                for thisComponent in blok2_2_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok2_2_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok2_rep_2.keys in ['', [], None]:  # No response was made
                    key_resp_blok2_rep_2.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok2_rep_2.corr = 1;  # correct non-response
                    else:
                       key_resp_blok2_rep_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_21 (TrialHandler)
                trials_21.addData('key_resp_blok2_rep_2.keys',key_resp_blok2_rep_2.keys)
                trials_21.addData('key_resp_blok2_rep_2.corr', key_resp_blok2_rep_2.corr)
                if key_resp_blok2_rep_2.keys != None:  # we had a response
                    trials_21.addData('key_resp_blok2_rep_2.rt', key_resp_blok2_rep_2.rt)
                    trials_21.addData('key_resp_blok2_rep_2.duration', key_resp_blok2_rep_2.duration)
                # Run 'End Routine' code from code_28
                if key_resp_blok2_rep_2.corr == 1:
                    rep_fdb2 = 0
                    trials_21.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok2_2_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_20 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_20')
                thisExp.addLoop(trials_20)  # add the loop to the experiment
                thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
                if thisTrial_20 != None:
                    for paramName in thisTrial_20:
                        globals()[paramName] = thisTrial_20[paramName]
                
                for thisTrial_20 in trials_20:
                    currentLoop = trials_20
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
                    if thisTrial_20 != None:
                        for paramName in thisTrial_20:
                            globals()[paramName] = thisTrial_20[paramName]
                    
                    # --- Prepare to start Routine "blok2_2_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok2_2_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_29
                    if key_resp_blok2_rep_2.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_6.setText(fdb2)
                    # keep track of which components have finished
                    blok2_2_rep_feedbackComponents = [text_rep_feed_6]
                    for thisComponent in blok2_2_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok2_2_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_6* updates
                        
                        # if text_rep_feed_6 is starting this frame...
                        if text_rep_feed_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_6.frameNStart = frameN  # exact frame index
                            text_rep_feed_6.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_6.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_6, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_6.started')
                            # update status
                            text_rep_feed_6.status = STARTED
                            text_rep_feed_6.setAutoDraw(True)
                        
                        # if text_rep_feed_6 is active this frame...
                        if text_rep_feed_6.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_6 is stopping this frame...
                        if text_rep_feed_6.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_6.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_6.tStop = t  # not accounting for scr refresh
                                text_rep_feed_6.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_6.stopped')
                                # update status
                                text_rep_feed_6.status = FINISHED
                                text_rep_feed_6.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok2_2_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok2_2_rep_feedback" ---
                    for thisComponent in blok2_2_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok2_2_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_20'
                
                # get names of stimulus parameters
                if trials_20.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_20.trialList[0].keys()
                # save data for this loop
                trials_20.saveAsText(filename + 'trials_20.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_21'
            
            # get names of stimulus parameters
            if trials_21.trialList in ([], [None], None):
                params = []
            else:
                params = trials_21.trialList[0].keys()
            # save data for this loop
            trials_21.saveAsText(filename + 'trials_21.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_blok2_2'
        
        # get names of stimulus parameters
        if loop_blok2_2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_blok2_2.trialList[0].keys()
        # save data for this loop
        loop_blok2_2.saveAsText(filename + 'loop_blok2_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok5_2_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok5_2_inst.started', globalClock.getTime())
        key_resp_blok5_inst_2.keys = []
        key_resp_blok5_inst_2.rt = []
        _key_resp_blok5_inst_2_allKeys = []
        # keep track of which components have finished
        blok5_2_instComponents = [text_blok5_ins_2, key_resp_blok5_inst_2]
        for thisComponent in blok5_2_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok5_2_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok5_ins_2* updates
            
            # if text_blok5_ins_2 is starting this frame...
            if text_blok5_ins_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok5_ins_2.frameNStart = frameN  # exact frame index
                text_blok5_ins_2.tStart = t  # local t and not account for scr refresh
                text_blok5_ins_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok5_ins_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok5_ins_2.started')
                # update status
                text_blok5_ins_2.status = STARTED
                text_blok5_ins_2.setAutoDraw(True)
            
            # if text_blok5_ins_2 is active this frame...
            if text_blok5_ins_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok5_inst_2* updates
            waitOnFlip = False
            
            # if key_resp_blok5_inst_2 is starting this frame...
            if key_resp_blok5_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok5_inst_2.frameNStart = frameN  # exact frame index
                key_resp_blok5_inst_2.tStart = t  # local t and not account for scr refresh
                key_resp_blok5_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok5_inst_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok5_inst_2.started')
                # update status
                key_resp_blok5_inst_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok5_inst_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok5_inst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok5_inst_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok5_inst_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok5_inst_2_allKeys.extend(theseKeys)
                if len(_key_resp_blok5_inst_2_allKeys):
                    key_resp_blok5_inst_2.keys = _key_resp_blok5_inst_2_allKeys[-1].name  # just the last key pressed
                    key_resp_blok5_inst_2.rt = _key_resp_blok5_inst_2_allKeys[-1].rt
                    key_resp_blok5_inst_2.duration = _key_resp_blok5_inst_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok5_2_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok5_2_inst" ---
        for thisComponent in blok5_2_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok5_2_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok5_inst_2.keys in ['', [], None]:  # No response was made
            key_resp_blok5_inst_2.keys = None
        condition2.addData('key_resp_blok5_inst_2.keys',key_resp_blok5_inst_2.keys)
        if key_resp_blok5_inst_2.keys != None:  # we had a response
            condition2.addData('key_resp_blok5_inst_2.rt', key_resp_blok5_inst_2.rt)
            condition2.addData('key_resp_blok5_inst_2.duration', key_resp_blok5_inst_2.duration)
        # the Routine "blok5_2_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_5_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block5Condition1.xlsx'),
            seed=None, name='loop_5_2')
        thisExp.addLoop(loop_5_2)  # add the loop to the experiment
        thisLoop_5_2 = loop_5_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_5_2.rgb)
        if thisLoop_5_2 != None:
            for paramName in thisLoop_5_2:
                globals()[paramName] = thisLoop_5_2[paramName]
        
        for thisLoop_5_2 in loop_5_2:
            currentLoop = loop_5_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_5_2.rgb)
            if thisLoop_5_2 != None:
                for paramName in thisLoop_5_2:
                    globals()[paramName] = thisLoop_5_2[paramName]
            
            # --- Prepare to start Routine "blok5_2_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok5_2_main.started', globalClock.getTime())
            target_image_blok5_3.setImage(ImageFiles)
            key_resp_blok5_main_2.keys = []
            key_resp_blok5_main_2.rt = []
            _key_resp_blok5_main_2_allKeys = []
            # keep track of which components have finished
            blok5_2_mainComponents = [target_image_blok5_3, key_resp_blok5_main_2, text_coveredattr_main5, text_uncoveredunattr_main5]
            for thisComponent in blok5_2_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok5_2_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok5_3* updates
                
                # if target_image_blok5_3 is starting this frame...
                if target_image_blok5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok5_3.frameNStart = frameN  # exact frame index
                    target_image_blok5_3.tStart = t  # local t and not account for scr refresh
                    target_image_blok5_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok5_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok5_3.started')
                    # update status
                    target_image_blok5_3.status = STARTED
                    target_image_blok5_3.setAutoDraw(True)
                
                # if target_image_blok5_3 is active this frame...
                if target_image_blok5_3.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok5_main_2* updates
                waitOnFlip = False
                
                # if key_resp_blok5_main_2 is starting this frame...
                if key_resp_blok5_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok5_main_2.frameNStart = frameN  # exact frame index
                    key_resp_blok5_main_2.tStart = t  # local t and not account for scr refresh
                    key_resp_blok5_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok5_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok5_main_2.started')
                    # update status
                    key_resp_blok5_main_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok5_main_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok5_main_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok5_main_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok5_main_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok5_main_2_allKeys.extend(theseKeys)
                    if len(_key_resp_blok5_main_2_allKeys):
                        key_resp_blok5_main_2.keys = _key_resp_blok5_main_2_allKeys[-1].name  # just the last key pressed
                        key_resp_blok5_main_2.rt = _key_resp_blok5_main_2_allKeys[-1].rt
                        key_resp_blok5_main_2.duration = _key_resp_blok5_main_2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok5_main_2.keys == str(corrAns)) or (key_resp_blok5_main_2.keys == corrAns):
                            key_resp_blok5_main_2.corr = 1
                        else:
                            key_resp_blok5_main_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_coveredattr_main5* updates
                
                # if text_coveredattr_main5 is starting this frame...
                if text_coveredattr_main5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_coveredattr_main5.frameNStart = frameN  # exact frame index
                    text_coveredattr_main5.tStart = t  # local t and not account for scr refresh
                    text_coveredattr_main5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_coveredattr_main5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_coveredattr_main5.started')
                    # update status
                    text_coveredattr_main5.status = STARTED
                    text_coveredattr_main5.setAutoDraw(True)
                
                # if text_coveredattr_main5 is active this frame...
                if text_coveredattr_main5.status == STARTED:
                    # update params
                    pass
                
                # *text_uncoveredunattr_main5* updates
                
                # if text_uncoveredunattr_main5 is starting this frame...
                if text_uncoveredunattr_main5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncoveredunattr_main5.frameNStart = frameN  # exact frame index
                    text_uncoveredunattr_main5.tStart = t  # local t and not account for scr refresh
                    text_uncoveredunattr_main5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncoveredunattr_main5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncoveredunattr_main5.started')
                    # update status
                    text_uncoveredunattr_main5.status = STARTED
                    text_uncoveredunattr_main5.setAutoDraw(True)
                
                # if text_uncoveredunattr_main5 is active this frame...
                if text_uncoveredunattr_main5.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok5_2_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok5_2_main" ---
            for thisComponent in blok5_2_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok5_2_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok5_main_2.keys in ['', [], None]:  # No response was made
                key_resp_blok5_main_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok5_main_2.corr = 1;  # correct non-response
                else:
                   key_resp_blok5_main_2.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_5_2 (TrialHandler)
            loop_5_2.addData('key_resp_blok5_main_2.keys',key_resp_blok5_main_2.keys)
            loop_5_2.addData('key_resp_blok5_main_2.corr', key_resp_blok5_main_2.corr)
            if key_resp_blok5_main_2.keys != None:  # we had a response
                loop_5_2.addData('key_resp_blok5_main_2.rt', key_resp_blok5_main_2.rt)
                loop_5_2.addData('key_resp_blok5_main_2.duration', key_resp_blok5_main_2.duration)
            # Run 'End Routine' code from code_30
            if key_resp_blok5_main_2.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok5_2_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_22 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_22')
            thisExp.addLoop(trials_22)  # add the loop to the experiment
            thisTrial_22 = trials_22.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
            if thisTrial_22 != None:
                for paramName in thisTrial_22:
                    globals()[paramName] = thisTrial_22[paramName]
            
            for thisTrial_22 in trials_22:
                currentLoop = trials_22
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
                if thisTrial_22 != None:
                    for paramName in thisTrial_22:
                        globals()[paramName] = thisTrial_22[paramName]
                
                # --- Prepare to start Routine "blok5_2_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok5_2_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_31
                if key_resp_blok5_main_2.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_9.setText(fdb)
                # keep track of which components have finished
                blok5_2_main_feedbackComponents = [text_fdb_9]
                for thisComponent in blok5_2_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok5_2_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_9* updates
                    
                    # if text_fdb_9 is starting this frame...
                    if text_fdb_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_9.frameNStart = frameN  # exact frame index
                        text_fdb_9.tStart = t  # local t and not account for scr refresh
                        text_fdb_9.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_9, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_9.started')
                        # update status
                        text_fdb_9.status = STARTED
                        text_fdb_9.setAutoDraw(True)
                    
                    # if text_fdb_9 is active this frame...
                    if text_fdb_9.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_9 is stopping this frame...
                    if text_fdb_9.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_9.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_9.tStop = t  # not accounting for scr refresh
                            text_fdb_9.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_9.stopped')
                            # update status
                            text_fdb_9.status = FINISHED
                            text_fdb_9.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok5_2_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok5_2_main_feedback" ---
                for thisComponent in blok5_2_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok5_2_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_22'
            
            # get names of stimulus parameters
            if trials_22.trialList in ([], [None], None):
                params = []
            else:
                params = trials_22.trialList[0].keys()
            # save data for this loop
            trials_22.saveAsText(filename + 'trials_22.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_24 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_24')
            thisExp.addLoop(trials_24)  # add the loop to the experiment
            thisTrial_24 = trials_24.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
            if thisTrial_24 != None:
                for paramName in thisTrial_24:
                    globals()[paramName] = thisTrial_24[paramName]
            
            for thisTrial_24 in trials_24:
                currentLoop = trials_24
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
                if thisTrial_24 != None:
                    for paramName in thisTrial_24:
                        globals()[paramName] = thisTrial_24[paramName]
                
                # --- Prepare to start Routine "blok5_2_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok5_2_rep.started', globalClock.getTime())
                target_image_blok5_rep_2.setImage(ImageFiles)
                key_resp_blok5_rep_2.keys = []
                key_resp_blok5_rep_2.rt = []
                _key_resp_blok5_rep_2_allKeys = []
                # keep track of which components have finished
                blok5_2_repComponents = [target_image_blok5_rep_2, key_resp_blok5_rep_2, text_coveredattr_rep_2, text_uncoveredunattr_rep_2]
                for thisComponent in blok5_2_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok5_2_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *target_image_blok5_rep_2* updates
                    
                    # if target_image_blok5_rep_2 is starting this frame...
                    if target_image_blok5_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        target_image_blok5_rep_2.frameNStart = frameN  # exact frame index
                        target_image_blok5_rep_2.tStart = t  # local t and not account for scr refresh
                        target_image_blok5_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_image_blok5_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_image_blok5_rep_2.started')
                        # update status
                        target_image_blok5_rep_2.status = STARTED
                        target_image_blok5_rep_2.setAutoDraw(True)
                    
                    # if target_image_blok5_rep_2 is active this frame...
                    if target_image_blok5_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok5_rep_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok5_rep_2 is starting this frame...
                    if key_resp_blok5_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok5_rep_2.frameNStart = frameN  # exact frame index
                        key_resp_blok5_rep_2.tStart = t  # local t and not account for scr refresh
                        key_resp_blok5_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok5_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok5_rep_2.started')
                        # update status
                        key_resp_blok5_rep_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok5_rep_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok5_rep_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok5_rep_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok5_rep_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok5_rep_2_allKeys.extend(theseKeys)
                        if len(_key_resp_blok5_rep_2_allKeys):
                            key_resp_blok5_rep_2.keys = _key_resp_blok5_rep_2_allKeys[-1].name  # just the last key pressed
                            key_resp_blok5_rep_2.rt = _key_resp_blok5_rep_2_allKeys[-1].rt
                            key_resp_blok5_rep_2.duration = _key_resp_blok5_rep_2_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok5_rep_2.keys == str(corrAns)) or (key_resp_blok5_rep_2.keys == corrAns):
                                key_resp_blok5_rep_2.corr = 1
                            else:
                                key_resp_blok5_rep_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_coveredattr_rep_2* updates
                    
                    # if text_coveredattr_rep_2 is starting this frame...
                    if text_coveredattr_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_coveredattr_rep_2.frameNStart = frameN  # exact frame index
                        text_coveredattr_rep_2.tStart = t  # local t and not account for scr refresh
                        text_coveredattr_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_coveredattr_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_coveredattr_rep_2.started')
                        # update status
                        text_coveredattr_rep_2.status = STARTED
                        text_coveredattr_rep_2.setAutoDraw(True)
                    
                    # if text_coveredattr_rep_2 is active this frame...
                    if text_coveredattr_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *text_uncoveredunattr_rep_2* updates
                    
                    # if text_uncoveredunattr_rep_2 is starting this frame...
                    if text_uncoveredunattr_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncoveredunattr_rep_2.frameNStart = frameN  # exact frame index
                        text_uncoveredunattr_rep_2.tStart = t  # local t and not account for scr refresh
                        text_uncoveredunattr_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncoveredunattr_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncoveredunattr_rep_2.started')
                        # update status
                        text_uncoveredunattr_rep_2.status = STARTED
                        text_uncoveredunattr_rep_2.setAutoDraw(True)
                    
                    # if text_uncoveredunattr_rep_2 is active this frame...
                    if text_uncoveredunattr_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok5_2_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok5_2_rep" ---
                for thisComponent in blok5_2_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok5_2_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok5_rep_2.keys in ['', [], None]:  # No response was made
                    key_resp_blok5_rep_2.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok5_rep_2.corr = 1;  # correct non-response
                    else:
                       key_resp_blok5_rep_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_24 (TrialHandler)
                trials_24.addData('key_resp_blok5_rep_2.keys',key_resp_blok5_rep_2.keys)
                trials_24.addData('key_resp_blok5_rep_2.corr', key_resp_blok5_rep_2.corr)
                if key_resp_blok5_rep_2.keys != None:  # we had a response
                    trials_24.addData('key_resp_blok5_rep_2.rt', key_resp_blok5_rep_2.rt)
                    trials_24.addData('key_resp_blok5_rep_2.duration', key_resp_blok5_rep_2.duration)
                # Run 'End Routine' code from code_32
                if key_resp_blok5_rep_2.corr == 1:
                    rep_fdb2 = 0
                    trials_24.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok5_2_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_23 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_23')
                thisExp.addLoop(trials_23)  # add the loop to the experiment
                thisTrial_23 = trials_23.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
                if thisTrial_23 != None:
                    for paramName in thisTrial_23:
                        globals()[paramName] = thisTrial_23[paramName]
                
                for thisTrial_23 in trials_23:
                    currentLoop = trials_23
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
                    if thisTrial_23 != None:
                        for paramName in thisTrial_23:
                            globals()[paramName] = thisTrial_23[paramName]
                    
                    # --- Prepare to start Routine "blok_5_2_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok_5_2_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_33
                    if key_resp_blok5_rep_2.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_7.setText(fdb2)
                    # keep track of which components have finished
                    blok_5_2_rep_feedbackComponents = [text_rep_feed_7]
                    for thisComponent in blok_5_2_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok_5_2_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_7* updates
                        
                        # if text_rep_feed_7 is starting this frame...
                        if text_rep_feed_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_7.frameNStart = frameN  # exact frame index
                            text_rep_feed_7.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_7.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_7, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_7.started')
                            # update status
                            text_rep_feed_7.status = STARTED
                            text_rep_feed_7.setAutoDraw(True)
                        
                        # if text_rep_feed_7 is active this frame...
                        if text_rep_feed_7.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_7 is stopping this frame...
                        if text_rep_feed_7.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_7.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_7.tStop = t  # not accounting for scr refresh
                                text_rep_feed_7.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_7.stopped')
                                # update status
                                text_rep_feed_7.status = FINISHED
                                text_rep_feed_7.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok_5_2_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok_5_2_rep_feedback" ---
                    for thisComponent in blok_5_2_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok_5_2_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_23'
                
                # get names of stimulus parameters
                if trials_23.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_23.trialList[0].keys()
                # save data for this loop
                trials_23.saveAsText(filename + 'trials_23.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_24'
            
            # get names of stimulus parameters
            if trials_24.trialList in ([], [None], None):
                params = []
            else:
                params = trials_24.trialList[0].keys()
            # save data for this loop
            trials_24.saveAsText(filename + 'trials_24.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_5_2'
        
        # get names of stimulus parameters
        if loop_5_2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_5_2.trialList[0].keys()
        # save data for this loop
        loop_5_2.saveAsText(filename + 'loop_5_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok1_2_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok1_2_inst.started', globalClock.getTime())
        key_resp_intr1_2.keys = []
        key_resp_intr1_2.rt = []
        _key_resp_intr1_2_allKeys = []
        # keep track of which components have finished
        blok1_2_instComponents = [text_blok1_instruction1_2, key_resp_intr1_2]
        for thisComponent in blok1_2_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok1_2_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok1_instruction1_2* updates
            
            # if text_blok1_instruction1_2 is starting this frame...
            if text_blok1_instruction1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok1_instruction1_2.frameNStart = frameN  # exact frame index
                text_blok1_instruction1_2.tStart = t  # local t and not account for scr refresh
                text_blok1_instruction1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok1_instruction1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok1_instruction1_2.started')
                # update status
                text_blok1_instruction1_2.status = STARTED
                text_blok1_instruction1_2.setAutoDraw(True)
            
            # if text_blok1_instruction1_2 is active this frame...
            if text_blok1_instruction1_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_intr1_2* updates
            waitOnFlip = False
            
            # if key_resp_intr1_2 is starting this frame...
            if key_resp_intr1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_intr1_2.frameNStart = frameN  # exact frame index
                key_resp_intr1_2.tStart = t  # local t and not account for scr refresh
                key_resp_intr1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_intr1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_intr1_2.started')
                # update status
                key_resp_intr1_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_intr1_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_intr1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_intr1_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_intr1_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_intr1_2_allKeys.extend(theseKeys)
                if len(_key_resp_intr1_2_allKeys):
                    key_resp_intr1_2.keys = _key_resp_intr1_2_allKeys[-1].name  # just the last key pressed
                    key_resp_intr1_2.rt = _key_resp_intr1_2_allKeys[-1].rt
                    key_resp_intr1_2.duration = _key_resp_intr1_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok1_2_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok1_2_inst" ---
        for thisComponent in blok1_2_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok1_2_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_intr1_2.keys in ['', [], None]:  # No response was made
            key_resp_intr1_2.keys = None
        condition2.addData('key_resp_intr1_2.keys',key_resp_intr1_2.keys)
        if key_resp_intr1_2.keys != None:  # we had a response
            condition2.addData('key_resp_intr1_2.rt', key_resp_intr1_2.rt)
            condition2.addData('key_resp_intr1_2.duration', key_resp_intr1_2.duration)
        # the Routine "blok1_2_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_blok1_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Conditions1.xlsx'),
            seed=None, name='loop_blok1_2')
        thisExp.addLoop(loop_blok1_2)  # add the loop to the experiment
        thisLoop_blok1_2 = loop_blok1_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok1_2.rgb)
        if thisLoop_blok1_2 != None:
            for paramName in thisLoop_blok1_2:
                globals()[paramName] = thisLoop_blok1_2[paramName]
        
        for thisLoop_blok1_2 in loop_blok1_2:
            currentLoop = loop_blok1_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok1_2.rgb)
            if thisLoop_blok1_2 != None:
                for paramName in thisLoop_blok1_2:
                    globals()[paramName] = thisLoop_blok1_2[paramName]
            
            # --- Prepare to start Routine "blok1_2_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok1_2_main.started', globalClock.getTime())
            target_image_blok1_2.setImage(ImageFile)
            key_resp_blok1_main_2.keys = []
            key_resp_blok1_main_2.rt = []
            _key_resp_blok1_main_2_allKeys = []
            # keep track of which components have finished
            blok1_2_mainComponents = [target_image_blok1_2, key_resp_blok1_main_2, text_uncovered_main_2, text_covered_main_2]
            for thisComponent in blok1_2_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok1_2_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok1_2* updates
                
                # if target_image_blok1_2 is starting this frame...
                if target_image_blok1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok1_2.frameNStart = frameN  # exact frame index
                    target_image_blok1_2.tStart = t  # local t and not account for scr refresh
                    target_image_blok1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok1_2.started')
                    # update status
                    target_image_blok1_2.status = STARTED
                    target_image_blok1_2.setAutoDraw(True)
                
                # if target_image_blok1_2 is active this frame...
                if target_image_blok1_2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok1_main_2* updates
                waitOnFlip = False
                
                # if key_resp_blok1_main_2 is starting this frame...
                if key_resp_blok1_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok1_main_2.frameNStart = frameN  # exact frame index
                    key_resp_blok1_main_2.tStart = t  # local t and not account for scr refresh
                    key_resp_blok1_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok1_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok1_main_2.started')
                    # update status
                    key_resp_blok1_main_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok1_main_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok1_main_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok1_main_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok1_main_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok1_main_2_allKeys.extend(theseKeys)
                    if len(_key_resp_blok1_main_2_allKeys):
                        key_resp_blok1_main_2.keys = _key_resp_blok1_main_2_allKeys[-1].name  # just the last key pressed
                        key_resp_blok1_main_2.rt = _key_resp_blok1_main_2_allKeys[-1].rt
                        key_resp_blok1_main_2.duration = _key_resp_blok1_main_2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok1_main_2.keys == str(corrAns)) or (key_resp_blok1_main_2.keys == corrAns):
                            key_resp_blok1_main_2.corr = 1
                        else:
                            key_resp_blok1_main_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_uncovered_main_2* updates
                
                # if text_uncovered_main_2 is starting this frame...
                if text_uncovered_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncovered_main_2.frameNStart = frameN  # exact frame index
                    text_uncovered_main_2.tStart = t  # local t and not account for scr refresh
                    text_uncovered_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncovered_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncovered_main_2.started')
                    # update status
                    text_uncovered_main_2.status = STARTED
                    text_uncovered_main_2.setAutoDraw(True)
                
                # if text_uncovered_main_2 is active this frame...
                if text_uncovered_main_2.status == STARTED:
                    # update params
                    pass
                
                # *text_covered_main_2* updates
                
                # if text_covered_main_2 is starting this frame...
                if text_covered_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_covered_main_2.frameNStart = frameN  # exact frame index
                    text_covered_main_2.tStart = t  # local t and not account for scr refresh
                    text_covered_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_covered_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_covered_main_2.started')
                    # update status
                    text_covered_main_2.status = STARTED
                    text_covered_main_2.setAutoDraw(True)
                
                # if text_covered_main_2 is active this frame...
                if text_covered_main_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok1_2_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok1_2_main" ---
            for thisComponent in blok1_2_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok1_2_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok1_main_2.keys in ['', [], None]:  # No response was made
                key_resp_blok1_main_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok1_main_2.corr = 1;  # correct non-response
                else:
                   key_resp_blok1_main_2.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_blok1_2 (TrialHandler)
            loop_blok1_2.addData('key_resp_blok1_main_2.keys',key_resp_blok1_main_2.keys)
            loop_blok1_2.addData('key_resp_blok1_main_2.corr', key_resp_blok1_main_2.corr)
            if key_resp_blok1_main_2.keys != None:  # we had a response
                loop_blok1_2.addData('key_resp_blok1_main_2.rt', key_resp_blok1_main_2.rt)
                loop_blok1_2.addData('key_resp_blok1_main_2.duration', key_resp_blok1_main_2.duration)
            # Run 'End Routine' code from code_34
            if key_resp_blok1_main_2.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok1_2_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_25 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_25')
            thisExp.addLoop(trials_25)  # add the loop to the experiment
            thisTrial_25 = trials_25.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
            if thisTrial_25 != None:
                for paramName in thisTrial_25:
                    globals()[paramName] = thisTrial_25[paramName]
            
            for thisTrial_25 in trials_25:
                currentLoop = trials_25
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
                if thisTrial_25 != None:
                    for paramName in thisTrial_25:
                        globals()[paramName] = thisTrial_25[paramName]
                
                # --- Prepare to start Routine "blok1_2_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok1_2_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_35
                if key_resp_blok1_main_2.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_10.setText(fdb)
                # keep track of which components have finished
                blok1_2_main_feedbackComponents = [text_fdb_10]
                for thisComponent in blok1_2_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok1_2_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_10* updates
                    
                    # if text_fdb_10 is starting this frame...
                    if text_fdb_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_10.frameNStart = frameN  # exact frame index
                        text_fdb_10.tStart = t  # local t and not account for scr refresh
                        text_fdb_10.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_10, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_10.started')
                        # update status
                        text_fdb_10.status = STARTED
                        text_fdb_10.setAutoDraw(True)
                    
                    # if text_fdb_10 is active this frame...
                    if text_fdb_10.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_10 is stopping this frame...
                    if text_fdb_10.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_10.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_10.tStop = t  # not accounting for scr refresh
                            text_fdb_10.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_10.stopped')
                            # update status
                            text_fdb_10.status = FINISHED
                            text_fdb_10.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok1_2_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok1_2_main_feedback" ---
                for thisComponent in blok1_2_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok1_2_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_25'
            
            # get names of stimulus parameters
            if trials_25.trialList in ([], [None], None):
                params = []
            else:
                params = trials_25.trialList[0].keys()
            # save data for this loop
            trials_25.saveAsText(filename + 'trials_25.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_27 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_27')
            thisExp.addLoop(trials_27)  # add the loop to the experiment
            thisTrial_27 = trials_27.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_27.rgb)
            if thisTrial_27 != None:
                for paramName in thisTrial_27:
                    globals()[paramName] = thisTrial_27[paramName]
            
            for thisTrial_27 in trials_27:
                currentLoop = trials_27
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_27.rgb)
                if thisTrial_27 != None:
                    for paramName in thisTrial_27:
                        globals()[paramName] = thisTrial_27[paramName]
                
                # --- Prepare to start Routine "blok1_2_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok1_2_rep.started', globalClock.getTime())
                image_blok1_rep_2.setImage(ImageFile)
                key_resp_blok1_rep_2.keys = []
                key_resp_blok1_rep_2.rt = []
                _key_resp_blok1_rep_2_allKeys = []
                # keep track of which components have finished
                blok1_2_repComponents = [image_blok1_rep_2, key_resp_blok1_rep_2, text_rep_uncovered_2, text_rep_covered_2]
                for thisComponent in blok1_2_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok1_2_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_blok1_rep_2* updates
                    
                    # if image_blok1_rep_2 is starting this frame...
                    if image_blok1_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_blok1_rep_2.frameNStart = frameN  # exact frame index
                        image_blok1_rep_2.tStart = t  # local t and not account for scr refresh
                        image_blok1_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_blok1_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_blok1_rep_2.started')
                        # update status
                        image_blok1_rep_2.status = STARTED
                        image_blok1_rep_2.setAutoDraw(True)
                    
                    # if image_blok1_rep_2 is active this frame...
                    if image_blok1_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok1_rep_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok1_rep_2 is starting this frame...
                    if key_resp_blok1_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok1_rep_2.frameNStart = frameN  # exact frame index
                        key_resp_blok1_rep_2.tStart = t  # local t and not account for scr refresh
                        key_resp_blok1_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok1_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok1_rep_2.started')
                        # update status
                        key_resp_blok1_rep_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok1_rep_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok1_rep_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok1_rep_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok1_rep_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok1_rep_2_allKeys.extend(theseKeys)
                        if len(_key_resp_blok1_rep_2_allKeys):
                            key_resp_blok1_rep_2.keys = _key_resp_blok1_rep_2_allKeys[-1].name  # just the last key pressed
                            key_resp_blok1_rep_2.rt = _key_resp_blok1_rep_2_allKeys[-1].rt
                            key_resp_blok1_rep_2.duration = _key_resp_blok1_rep_2_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok1_rep_2.keys == str(corrAns)) or (key_resp_blok1_rep_2.keys == corrAns):
                                key_resp_blok1_rep_2.corr = 1
                            else:
                                key_resp_blok1_rep_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_rep_uncovered_2* updates
                    
                    # if text_rep_uncovered_2 is starting this frame...
                    if text_rep_uncovered_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_rep_uncovered_2.frameNStart = frameN  # exact frame index
                        text_rep_uncovered_2.tStart = t  # local t and not account for scr refresh
                        text_rep_uncovered_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_rep_uncovered_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_rep_uncovered_2.started')
                        # update status
                        text_rep_uncovered_2.status = STARTED
                        text_rep_uncovered_2.setAutoDraw(True)
                    
                    # if text_rep_uncovered_2 is active this frame...
                    if text_rep_uncovered_2.status == STARTED:
                        # update params
                        pass
                    
                    # *text_rep_covered_2* updates
                    
                    # if text_rep_covered_2 is starting this frame...
                    if text_rep_covered_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_rep_covered_2.frameNStart = frameN  # exact frame index
                        text_rep_covered_2.tStart = t  # local t and not account for scr refresh
                        text_rep_covered_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_rep_covered_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_rep_covered_2.started')
                        # update status
                        text_rep_covered_2.status = STARTED
                        text_rep_covered_2.setAutoDraw(True)
                    
                    # if text_rep_covered_2 is active this frame...
                    if text_rep_covered_2.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok1_2_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok1_2_rep" ---
                for thisComponent in blok1_2_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok1_2_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok1_rep_2.keys in ['', [], None]:  # No response was made
                    key_resp_blok1_rep_2.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok1_rep_2.corr = 1;  # correct non-response
                    else:
                       key_resp_blok1_rep_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_27 (TrialHandler)
                trials_27.addData('key_resp_blok1_rep_2.keys',key_resp_blok1_rep_2.keys)
                trials_27.addData('key_resp_blok1_rep_2.corr', key_resp_blok1_rep_2.corr)
                if key_resp_blok1_rep_2.keys != None:  # we had a response
                    trials_27.addData('key_resp_blok1_rep_2.rt', key_resp_blok1_rep_2.rt)
                    trials_27.addData('key_resp_blok1_rep_2.duration', key_resp_blok1_rep_2.duration)
                # Run 'End Routine' code from code_36
                if key_resp_blok1_rep_2.corr == 1:
                    rep_fdb2 = 0
                    trials_27.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok1_2_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_26 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_26')
                thisExp.addLoop(trials_26)  # add the loop to the experiment
                thisTrial_26 = trials_26.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
                if thisTrial_26 != None:
                    for paramName in thisTrial_26:
                        globals()[paramName] = thisTrial_26[paramName]
                
                for thisTrial_26 in trials_26:
                    currentLoop = trials_26
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
                    if thisTrial_26 != None:
                        for paramName in thisTrial_26:
                            globals()[paramName] = thisTrial_26[paramName]
                    
                    # --- Prepare to start Routine "blok1_2_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok1_2_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_37
                    if key_resp_blok1_rep_2.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_8.setText(fdb2)
                    # keep track of which components have finished
                    blok1_2_rep_feedbackComponents = [text_rep_feed_8]
                    for thisComponent in blok1_2_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok1_2_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_8* updates
                        
                        # if text_rep_feed_8 is starting this frame...
                        if text_rep_feed_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_8.frameNStart = frameN  # exact frame index
                            text_rep_feed_8.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_8.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_8, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_8.started')
                            # update status
                            text_rep_feed_8.status = STARTED
                            text_rep_feed_8.setAutoDraw(True)
                        
                        # if text_rep_feed_8 is active this frame...
                        if text_rep_feed_8.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_8 is stopping this frame...
                        if text_rep_feed_8.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_8.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_8.tStop = t  # not accounting for scr refresh
                                text_rep_feed_8.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_8.stopped')
                                # update status
                                text_rep_feed_8.status = FINISHED
                                text_rep_feed_8.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok1_2_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok1_2_rep_feedback" ---
                    for thisComponent in blok1_2_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok1_2_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_26'
                
                # get names of stimulus parameters
                if trials_26.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_26.trialList[0].keys()
                # save data for this loop
                trials_26.saveAsText(filename + 'trials_26.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_27'
            
            # get names of stimulus parameters
            if trials_27.trialList in ([], [None], None):
                params = []
            else:
                params = trials_27.trialList[0].keys()
            # save data for this loop
            trials_27.saveAsText(filename + 'trials_27.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_blok1_2'
        
        # get names of stimulus parameters
        if loop_blok1_2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_blok1_2.trialList[0].keys()
        # save data for this loop
        loop_blok1_2.saveAsText(filename + 'loop_blok1_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "blok3_2_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blok3_2_inst.started', globalClock.getTime())
        key_resp_blok3_inst_2.keys = []
        key_resp_blok3_inst_2.rt = []
        _key_resp_blok3_inst_2_allKeys = []
        # keep track of which components have finished
        blok3_2_instComponents = [text_blok3_ins_2, key_resp_blok3_inst_2]
        for thisComponent in blok3_2_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blok3_2_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blok3_ins_2* updates
            
            # if text_blok3_ins_2 is starting this frame...
            if text_blok3_ins_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blok3_ins_2.frameNStart = frameN  # exact frame index
                text_blok3_ins_2.tStart = t  # local t and not account for scr refresh
                text_blok3_ins_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blok3_ins_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blok3_ins_2.started')
                # update status
                text_blok3_ins_2.status = STARTED
                text_blok3_ins_2.setAutoDraw(True)
            
            # if text_blok3_ins_2 is active this frame...
            if text_blok3_ins_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_blok3_inst_2* updates
            waitOnFlip = False
            
            # if key_resp_blok3_inst_2 is starting this frame...
            if key_resp_blok3_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_blok3_inst_2.frameNStart = frameN  # exact frame index
                key_resp_blok3_inst_2.tStart = t  # local t and not account for scr refresh
                key_resp_blok3_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_blok3_inst_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_blok3_inst_2.started')
                # update status
                key_resp_blok3_inst_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_blok3_inst_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_blok3_inst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_blok3_inst_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_blok3_inst_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_blok3_inst_2_allKeys.extend(theseKeys)
                if len(_key_resp_blok3_inst_2_allKeys):
                    key_resp_blok3_inst_2.keys = _key_resp_blok3_inst_2_allKeys[-1].name  # just the last key pressed
                    key_resp_blok3_inst_2.rt = _key_resp_blok3_inst_2_allKeys[-1].rt
                    key_resp_blok3_inst_2.duration = _key_resp_blok3_inst_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blok3_2_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blok3_2_inst" ---
        for thisComponent in blok3_2_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blok3_2_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_blok3_inst_2.keys in ['', [], None]:  # No response was made
            key_resp_blok3_inst_2.keys = None
        condition2.addData('key_resp_blok3_inst_2.keys',key_resp_blok3_inst_2.keys)
        if key_resp_blok3_inst_2.keys != None:  # we had a response
            condition2.addData('key_resp_blok3_inst_2.rt', key_resp_blok3_inst_2.rt)
            condition2.addData('key_resp_blok3_inst_2.duration', key_resp_blok3_inst_2.duration)
        # the Routine "blok3_2_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_blok3_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Block3Condition1.xlsx'),
            seed=None, name='loop_blok3_2')
        thisExp.addLoop(loop_blok3_2)  # add the loop to the experiment
        thisLoop_blok3_2 = loop_blok3_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok3_2.rgb)
        if thisLoop_blok3_2 != None:
            for paramName in thisLoop_blok3_2:
                globals()[paramName] = thisLoop_blok3_2[paramName]
        
        for thisLoop_blok3_2 in loop_blok3_2:
            currentLoop = loop_blok3_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_blok3_2.rgb)
            if thisLoop_blok3_2 != None:
                for paramName in thisLoop_blok3_2:
                    globals()[paramName] = thisLoop_blok3_2[paramName]
            
            # --- Prepare to start Routine "blok3_2_main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('blok3_2_main.started', globalClock.getTime())
            target_image_blok3_2.setImage(ImageFiles)
            key_resp_blok3_main_2.keys = []
            key_resp_blok3_main_2.rt = []
            _key_resp_blok3_main_2_allKeys = []
            # keep track of which components have finished
            blok3_2_mainComponents = [target_image_blok3_2, key_resp_blok3_main_2, text_uncoveredattr_main_2, text_coveredunattr_main_2]
            for thisComponent in blok3_2_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blok3_2_main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image_blok3_2* updates
                
                # if target_image_blok3_2 is starting this frame...
                if target_image_blok3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image_blok3_2.frameNStart = frameN  # exact frame index
                    target_image_blok3_2.tStart = t  # local t and not account for scr refresh
                    target_image_blok3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image_blok3_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_image_blok3_2.started')
                    # update status
                    target_image_blok3_2.status = STARTED
                    target_image_blok3_2.setAutoDraw(True)
                
                # if target_image_blok3_2 is active this frame...
                if target_image_blok3_2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_blok3_main_2* updates
                waitOnFlip = False
                
                # if key_resp_blok3_main_2 is starting this frame...
                if key_resp_blok3_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_blok3_main_2.frameNStart = frameN  # exact frame index
                    key_resp_blok3_main_2.tStart = t  # local t and not account for scr refresh
                    key_resp_blok3_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_blok3_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_blok3_main_2.started')
                    # update status
                    key_resp_blok3_main_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_blok3_main_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_blok3_main_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_blok3_main_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_blok3_main_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_blok3_main_2_allKeys.extend(theseKeys)
                    if len(_key_resp_blok3_main_2_allKeys):
                        key_resp_blok3_main_2.keys = _key_resp_blok3_main_2_allKeys[-1].name  # just the last key pressed
                        key_resp_blok3_main_2.rt = _key_resp_blok3_main_2_allKeys[-1].rt
                        key_resp_blok3_main_2.duration = _key_resp_blok3_main_2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_blok3_main_2.keys == str(corrAns)) or (key_resp_blok3_main_2.keys == corrAns):
                            key_resp_blok3_main_2.corr = 1
                        else:
                            key_resp_blok3_main_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_uncoveredattr_main_2* updates
                
                # if text_uncoveredattr_main_2 is starting this frame...
                if text_uncoveredattr_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_uncoveredattr_main_2.frameNStart = frameN  # exact frame index
                    text_uncoveredattr_main_2.tStart = t  # local t and not account for scr refresh
                    text_uncoveredattr_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_uncoveredattr_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_uncoveredattr_main_2.started')
                    # update status
                    text_uncoveredattr_main_2.status = STARTED
                    text_uncoveredattr_main_2.setAutoDraw(True)
                
                # if text_uncoveredattr_main_2 is active this frame...
                if text_uncoveredattr_main_2.status == STARTED:
                    # update params
                    pass
                
                # *text_coveredunattr_main_2* updates
                
                # if text_coveredunattr_main_2 is starting this frame...
                if text_coveredunattr_main_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_coveredunattr_main_2.frameNStart = frameN  # exact frame index
                    text_coveredunattr_main_2.tStart = t  # local t and not account for scr refresh
                    text_coveredunattr_main_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_coveredunattr_main_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_coveredunattr_main_2.started')
                    # update status
                    text_coveredunattr_main_2.status = STARTED
                    text_coveredunattr_main_2.setAutoDraw(True)
                
                # if text_coveredunattr_main_2 is active this frame...
                if text_coveredunattr_main_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blok3_2_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blok3_2_main" ---
            for thisComponent in blok3_2_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('blok3_2_main.stopped', globalClock.getTime())
            # check responses
            if key_resp_blok3_main_2.keys in ['', [], None]:  # No response was made
                key_resp_blok3_main_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp_blok3_main_2.corr = 1;  # correct non-response
                else:
                   key_resp_blok3_main_2.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_blok3_2 (TrialHandler)
            loop_blok3_2.addData('key_resp_blok3_main_2.keys',key_resp_blok3_main_2.keys)
            loop_blok3_2.addData('key_resp_blok3_main_2.corr', key_resp_blok3_main_2.corr)
            if key_resp_blok3_main_2.keys != None:  # we had a response
                loop_blok3_2.addData('key_resp_blok3_main_2.rt', key_resp_blok3_main_2.rt)
                loop_blok3_2.addData('key_resp_blok3_main_2.duration', key_resp_blok3_main_2.duration)
            # Run 'End Routine' code from code_38
            if key_resp_blok3_main_2.corr == 1:
                rep_fdb1 = 0
                mynreps = 0
            else:
                rep_fdb1 = 1
            # the Routine "blok3_2_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_28 = data.TrialHandler(nReps=rep_fdb1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_28')
            thisExp.addLoop(trials_28)  # add the loop to the experiment
            thisTrial_28 = trials_28.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_28.rgb)
            if thisTrial_28 != None:
                for paramName in thisTrial_28:
                    globals()[paramName] = thisTrial_28[paramName]
            
            for thisTrial_28 in trials_28:
                currentLoop = trials_28
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_28.rgb)
                if thisTrial_28 != None:
                    for paramName in thisTrial_28:
                        globals()[paramName] = thisTrial_28[paramName]
                
                # --- Prepare to start Routine "blok3_2_main_feedback" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok3_2_main_feedback.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_39
                if key_resp_blok3_main_2.corr == 1:
                    fdb = "correct"
                    
                else:
                    fdb = "X" 
                    mynreps = 1000
                text_fdb_11.setText(fdb)
                # keep track of which components have finished
                blok3_2_main_feedbackComponents = [text_fdb_11]
                for thisComponent in blok3_2_main_feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok3_2_main_feedback" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_fdb_11* updates
                    
                    # if text_fdb_11 is starting this frame...
                    if text_fdb_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_fdb_11.frameNStart = frameN  # exact frame index
                        text_fdb_11.tStart = t  # local t and not account for scr refresh
                        text_fdb_11.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_fdb_11, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fdb_11.started')
                        # update status
                        text_fdb_11.status = STARTED
                        text_fdb_11.setAutoDraw(True)
                    
                    # if text_fdb_11 is active this frame...
                    if text_fdb_11.status == STARTED:
                        # update params
                        pass
                    
                    # if text_fdb_11 is stopping this frame...
                    if text_fdb_11.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_fdb_11.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_fdb_11.tStop = t  # not accounting for scr refresh
                            text_fdb_11.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_fdb_11.stopped')
                            # update status
                            text_fdb_11.status = FINISHED
                            text_fdb_11.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok3_2_main_feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok3_2_main_feedback" ---
                for thisComponent in blok3_2_main_feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok3_2_main_feedback.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_fdb1 repeats of 'trials_28'
            
            # get names of stimulus parameters
            if trials_28.trialList in ([], [None], None):
                params = []
            else:
                params = trials_28.trialList[0].keys()
            # save data for this loop
            trials_28.saveAsText(filename + 'trials_28.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            trials_30 = data.TrialHandler(nReps=mynreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_30')
            thisExp.addLoop(trials_30)  # add the loop to the experiment
            thisTrial_30 = trials_30.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_30.rgb)
            if thisTrial_30 != None:
                for paramName in thisTrial_30:
                    globals()[paramName] = thisTrial_30[paramName]
            
            for thisTrial_30 in trials_30:
                currentLoop = trials_30
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_30.rgb)
                if thisTrial_30 != None:
                    for paramName in thisTrial_30:
                        globals()[paramName] = thisTrial_30[paramName]
                
                # --- Prepare to start Routine "blok3_2_rep" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('blok3_2_rep.started', globalClock.getTime())
                image_blok3_main1_rep_2.setImage(ImageFiles)
                key_resp_blok3_main1_rep_2.keys = []
                key_resp_blok3_main1_rep_2.rt = []
                _key_resp_blok3_main1_rep_2_allKeys = []
                # keep track of which components have finished
                blok3_2_repComponents = [image_blok3_main1_rep_2, key_resp_blok3_main1_rep_2, text_uncoveredattr_main_rep_2, text_coveredunattr_main_rep_2]
                for thisComponent in blok3_2_repComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blok3_2_rep" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_blok3_main1_rep_2* updates
                    
                    # if image_blok3_main1_rep_2 is starting this frame...
                    if image_blok3_main1_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_blok3_main1_rep_2.frameNStart = frameN  # exact frame index
                        image_blok3_main1_rep_2.tStart = t  # local t and not account for scr refresh
                        image_blok3_main1_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_blok3_main1_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_blok3_main1_rep_2.started')
                        # update status
                        image_blok3_main1_rep_2.status = STARTED
                        image_blok3_main1_rep_2.setAutoDraw(True)
                    
                    # if image_blok3_main1_rep_2 is active this frame...
                    if image_blok3_main1_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_blok3_main1_rep_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_blok3_main1_rep_2 is starting this frame...
                    if key_resp_blok3_main1_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_blok3_main1_rep_2.frameNStart = frameN  # exact frame index
                        key_resp_blok3_main1_rep_2.tStart = t  # local t and not account for scr refresh
                        key_resp_blok3_main1_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_blok3_main1_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_blok3_main1_rep_2.started')
                        # update status
                        key_resp_blok3_main1_rep_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_blok3_main1_rep_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_blok3_main1_rep_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_blok3_main1_rep_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_blok3_main1_rep_2.getKeys(keyList=['e','i'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_blok3_main1_rep_2_allKeys.extend(theseKeys)
                        if len(_key_resp_blok3_main1_rep_2_allKeys):
                            key_resp_blok3_main1_rep_2.keys = _key_resp_blok3_main1_rep_2_allKeys[-1].name  # just the last key pressed
                            key_resp_blok3_main1_rep_2.rt = _key_resp_blok3_main1_rep_2_allKeys[-1].rt
                            key_resp_blok3_main1_rep_2.duration = _key_resp_blok3_main1_rep_2_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_blok3_main1_rep_2.keys == str(corrAns)) or (key_resp_blok3_main1_rep_2.keys == corrAns):
                                key_resp_blok3_main1_rep_2.corr = 1
                            else:
                                key_resp_blok3_main1_rep_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_uncoveredattr_main_rep_2* updates
                    
                    # if text_uncoveredattr_main_rep_2 is starting this frame...
                    if text_uncoveredattr_main_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_uncoveredattr_main_rep_2.frameNStart = frameN  # exact frame index
                        text_uncoveredattr_main_rep_2.tStart = t  # local t and not account for scr refresh
                        text_uncoveredattr_main_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_uncoveredattr_main_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_uncoveredattr_main_rep_2.started')
                        # update status
                        text_uncoveredattr_main_rep_2.status = STARTED
                        text_uncoveredattr_main_rep_2.setAutoDraw(True)
                    
                    # if text_uncoveredattr_main_rep_2 is active this frame...
                    if text_uncoveredattr_main_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # *text_coveredunattr_main_rep_2* updates
                    
                    # if text_coveredunattr_main_rep_2 is starting this frame...
                    if text_coveredunattr_main_rep_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_coveredunattr_main_rep_2.frameNStart = frameN  # exact frame index
                        text_coveredunattr_main_rep_2.tStart = t  # local t and not account for scr refresh
                        text_coveredunattr_main_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_coveredunattr_main_rep_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_coveredunattr_main_rep_2.started')
                        # update status
                        text_coveredunattr_main_rep_2.status = STARTED
                        text_coveredunattr_main_rep_2.setAutoDraw(True)
                    
                    # if text_coveredunattr_main_rep_2 is active this frame...
                    if text_coveredunattr_main_rep_2.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blok3_2_repComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blok3_2_rep" ---
                for thisComponent in blok3_2_repComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('blok3_2_rep.stopped', globalClock.getTime())
                # check responses
                if key_resp_blok3_main1_rep_2.keys in ['', [], None]:  # No response was made
                    key_resp_blok3_main1_rep_2.keys = None
                    # was no response the correct answer?!
                    if str(corrAns).lower() == 'none':
                       key_resp_blok3_main1_rep_2.corr = 1;  # correct non-response
                    else:
                       key_resp_blok3_main1_rep_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_30 (TrialHandler)
                trials_30.addData('key_resp_blok3_main1_rep_2.keys',key_resp_blok3_main1_rep_2.keys)
                trials_30.addData('key_resp_blok3_main1_rep_2.corr', key_resp_blok3_main1_rep_2.corr)
                if key_resp_blok3_main1_rep_2.keys != None:  # we had a response
                    trials_30.addData('key_resp_blok3_main1_rep_2.rt', key_resp_blok3_main1_rep_2.rt)
                    trials_30.addData('key_resp_blok3_main1_rep_2.duration', key_resp_blok3_main1_rep_2.duration)
                # Run 'End Routine' code from code_40
                if key_resp_blok3_main1_rep_2.corr == 1:
                    rep_fdb2 = 0
                    trials_30.finished = True
                else:
                    rep_fdb2 = 1
                # the Routine "blok3_2_rep" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_29 = data.TrialHandler(nReps=rep_fdb2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_29')
                thisExp.addLoop(trials_29)  # add the loop to the experiment
                thisTrial_29 = trials_29.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
                if thisTrial_29 != None:
                    for paramName in thisTrial_29:
                        globals()[paramName] = thisTrial_29[paramName]
                
                for thisTrial_29 in trials_29:
                    currentLoop = trials_29
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
                    if thisTrial_29 != None:
                        for paramName in thisTrial_29:
                            globals()[paramName] = thisTrial_29[paramName]
                    
                    # --- Prepare to start Routine "blok3_2_rep_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('blok3_2_rep_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from code_41
                    if key_resp_blok3_main1_rep_2.corr == 1:
                        fdb2 = "correct"
                    else:
                        fdb2 = "X" 
                    text_rep_feed_9.setText(fdb2)
                    # keep track of which components have finished
                    blok3_2_rep_feedbackComponents = [text_rep_feed_9]
                    for thisComponent in blok3_2_rep_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "blok3_2_rep_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_rep_feed_9* updates
                        
                        # if text_rep_feed_9 is starting this frame...
                        if text_rep_feed_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_rep_feed_9.frameNStart = frameN  # exact frame index
                            text_rep_feed_9.tStart = t  # local t and not account for scr refresh
                            text_rep_feed_9.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_rep_feed_9, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_rep_feed_9.started')
                            # update status
                            text_rep_feed_9.status = STARTED
                            text_rep_feed_9.setAutoDraw(True)
                        
                        # if text_rep_feed_9 is active this frame...
                        if text_rep_feed_9.status == STARTED:
                            # update params
                            pass
                        
                        # if text_rep_feed_9 is stopping this frame...
                        if text_rep_feed_9.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_rep_feed_9.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                text_rep_feed_9.tStop = t  # not accounting for scr refresh
                                text_rep_feed_9.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'text_rep_feed_9.stopped')
                                # update status
                                text_rep_feed_9.status = FINISHED
                                text_rep_feed_9.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in blok3_2_rep_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "blok3_2_rep_feedback" ---
                    for thisComponent in blok3_2_rep_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('blok3_2_rep_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed rep_fdb2 repeats of 'trials_29'
                
                # get names of stimulus parameters
                if trials_29.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials_29.trialList[0].keys()
                # save data for this loop
                trials_29.saveAsText(filename + 'trials_29.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed mynreps repeats of 'trials_30'
            
            # get names of stimulus parameters
            if trials_30.trialList in ([], [None], None):
                params = []
            else:
                params = trials_30.trialList[0].keys()
            # save data for this loop
            trials_30.saveAsText(filename + 'trials_30.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'loop_blok3_2'
        
        # get names of stimulus parameters
        if loop_blok3_2.trialList in ([], [None], None):
            params = []
        else:
            params = loop_blok3_2.trialList[0].keys()
        # save data for this loop
        loop_blok3_2.saveAsText(filename + 'loop_blok3_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "thanks2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('thanks2.started', globalClock.getTime())
        key_resp_thanks2.keys = []
        key_resp_thanks2.rt = []
        _key_resp_thanks2_allKeys = []
        # keep track of which components have finished
        thanks2Components = [text__thanks2, key_resp_thanks2]
        for thisComponent in thanks2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "thanks2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text__thanks2* updates
            
            # if text__thanks2 is starting this frame...
            if text__thanks2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text__thanks2.frameNStart = frameN  # exact frame index
                text__thanks2.tStart = t  # local t and not account for scr refresh
                text__thanks2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text__thanks2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text__thanks2.started')
                # update status
                text__thanks2.status = STARTED
                text__thanks2.setAutoDraw(True)
            
            # if text__thanks2 is active this frame...
            if text__thanks2.status == STARTED:
                # update params
                pass
            
            # *key_resp_thanks2* updates
            waitOnFlip = False
            
            # if key_resp_thanks2 is starting this frame...
            if key_resp_thanks2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_thanks2.frameNStart = frameN  # exact frame index
                key_resp_thanks2.tStart = t  # local t and not account for scr refresh
                key_resp_thanks2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_thanks2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_thanks2.started')
                # update status
                key_resp_thanks2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_thanks2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_thanks2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_thanks2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_thanks2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_thanks2_allKeys.extend(theseKeys)
                if len(_key_resp_thanks2_allKeys):
                    key_resp_thanks2.keys = _key_resp_thanks2_allKeys[-1].name  # just the last key pressed
                    key_resp_thanks2.rt = _key_resp_thanks2_allKeys[-1].rt
                    key_resp_thanks2.duration = _key_resp_thanks2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in thanks2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "thanks2" ---
        for thisComponent in thanks2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('thanks2.stopped', globalClock.getTime())
        # check responses
        if key_resp_thanks2.keys in ['', [], None]:  # No response was made
            key_resp_thanks2.keys = None
        condition2.addData('key_resp_thanks2.keys',key_resp_thanks2.keys)
        if key_resp_thanks2.keys != None:  # we had a response
            condition2.addData('key_resp_thanks2.rt', key_resp_thanks2.rt)
            condition2.addData('key_resp_thanks2.duration', key_resp_thanks2.duration)
        # the Routine "thanks2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "exitcode2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('exitcode2.started', globalClock.getTime())
        # keep track of which components have finished
        exitcode2Components = []
        for thisComponent in exitcode2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exitcode2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from exitcode_2
            print("Experiment has ended")
            core.quit()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exitcode2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exitcode2" ---
        for thisComponent in exitcode2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('exitcode2.stopped', globalClock.getTime())
        # the Routine "exitcode2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed nRepsB repeats of 'condition2'
    
    # get names of stimulus parameters
    if condition2.trialList in ([], [None], None):
        params = []
    else:
        params = condition2.trialList[0].keys()
    # save data for this loop
    condition2.saveAsText(filename + 'condition2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='tab')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
