import os
import datetime
from CRABClient.UserUtilities import config
config = config()

todaysDate = datetime.date.today().strftime('%Y%m%d')

config.General.requestName = f'ScoutingNano_DYto2L_withAXOscore_{todaysDate}'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = '/afs/cern.ch/user/e/ekauffma/crabWorkArea'

config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/scoutingnano_crab/scoutingnano_mc.py'
config.JobType.pluginName = 'Analysis'
config.Data.outLFNDirBase = '/store/user/ekauffma/'

config.JobType.maxMemoryMB = 5000

config.Data.inputDataset = '/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24MiniAOD-KeepSi_133X_mcRun3_2024_realistic_v8-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.publication = False
config.Data.outputDatasetTag = f'ScoutingNano_DYto2L_withAXOscore_{todaysDate}'
config.Data.partialDataset = True

config.Site.storageSite = 'T2_CH_CERN'
config.Data.outLFNDirBase = '/store/group/phys_exotica/axol1tl/MC_ScoutingNano_withAXOscore/'
