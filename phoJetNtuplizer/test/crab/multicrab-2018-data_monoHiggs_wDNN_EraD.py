import os

dataset = {
  'MET2018A' : '/MET/Run2018A-17Sep2018-v1/MINIAOD',
  'MET2018B' : '/MET/Run2018A-17Sep2018-v1/MINIAOD',
  'MET2018C' : '/MET/Run2018C-17Sep2018-v1/MINIAOD',

  'EGamma2018A' : '/EGamma/Run2018A-17Sep2018-v2/MINIAOD',
  'EGamma2018B' : '/EGamma/Run2018B-17Sep2018-v1/MINIAOD',
  'EGamma2018C' : '/EGamma/Run2018C-17Sep2018-v1/MINIAOD',
  'EGamma2018D' : '/EGamma/Run2018D-22Jan2019-v2/MINIAOD',

  'SingleMuonA' : '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD',
  'SingleMuonB' : '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD',
  'SingleMuonC' : '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD', 
  'SingleMuonD_PromptReco' : '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD', 
  'SingleMuonD' : '/SingleMuon/Run2018D-30Apr2019-v1/MINIAOD',
  
  'TauA' : '/Tau/Run2018A-17Sep2018-v1/MINIAOD',
  'TauB' : '/Tau/Run2018B-17Sep2018-v1/MINIAOD', 
  'TauC' : '/Tau/Run2018C-17Sep2018-v1/MINIAOD', 
  'TauD_PromptReco' : '/Tau/Run2018D-PromptReco-v2/MINIAOD', 
  
  'JetHT2018A' : '/JetHT/Run2018A-17Sep2018-v1/MINIAOD',
  'JetHT2018B' : '/JetHT/Run2018B-17Sep2018-v1/MINIAOD',
  'JetHT2018C' : '/JetHT/Run2018C-17Sep2018-v1/MINIAOD',
}

#if __name__ == '__main__':
from CRABAPI.RawCommand import crabCommand

def submit(config):
  res = crabCommand('submit', config = config)

from CRABClient.UserUtilities import config
from multiprocessing import Process

config = config()
name = 'data2018_13Mar2020'
config.General.workArea = 'crab_'+name
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['Autumn18_RunABCD_V19_DATA.db']
config.JobType.allowUndistributedCMSSW = True

config.section_('Data') 
config.Data.publication = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.lumiMask = '/afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/phoJetAnalysis/phoJetNtuplizer/test/Cert_314472-325175_13TeV_17SeptEarlyReReco2018D_Collisions18_JSON.txt'

config.Site.storageSite = 'T2_US_Wisconsin'
#config.Site.whitelist = ["T2_US_Wisconsin"]
#config.Site.blacklist = ['T2_CH_CERN']

#listOfSamples = ['MET2018A', 'MET2018B', 'MET2018C']
listOfSamples = ['EGamma2018D', 'SingleMuonD_PromptReco', 'TauD_PromptReco' ]
listofSections =['_1', '_2', '_3']

for sample in listOfSamples:  
  for iSection in listofSections:
    os.popen('cp run_102X_data2018.py run_102X_data2018_'+sample+iSection+'.py')
    with open('run_102X_data2018_'+sample+iSection+'.py') as oldFile:
      newText = oldFile.read().replace('Ntuple_data2018.root', 'Ntuple_data2018_'+sample+'.root')
    with open('run_102X_data2018_'+sample+iSection+'.py', 'w') as newFile:
      newFile.write(newText)
      
    config.General.requestName = 'job_'+sample+iSection
    
    config.JobType.psetName = 'run_102X_data2018_'+sample+iSection+'.py'
    config.JobType.outputFiles = ['Ntuple_data2018_'+sample+'.root']
    
    config.Data.inputDataset   = dataset[sample]
    config.Data.unitsPerJob = 13
    config.Data.totalUnits = -1
    config.Data.outLFNDirBase = '/store/user/jmadhusu/'+name
    config.Data.lumiMask = '/afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/phoJetAnalysis/phoJetNtuplizer/test/Cert_314472-325175_13TeV_17SeptEarlyReReco2018D_Collisions18_JSON'+iSection+'.txt'
    
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
    
