timestamps {

node ('cloud') { 

	stage ('test-build - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/dzup4uk/feed-parser.git']]]) 
	}
	stage ('test-build - Build') {
 	
// Unable to convert a build step referring to "hudson.plugins.timestamper.TimestamperBuildWrapper". Please verify and convert manually if required.		// Shell build step
sh """ 
apt-get -y update && apt-get -y install python3 python3-pip 
pip3 install pylint
pip3 install -r requirements.txt
pylint scraper.py
python3 -V
python3 scraper.py 
 """
		archiveArtifacts allowEmptyArchive: false, artifacts: 'index.html', caseSensitive: true, defaultExcludes: true, fingerprint: false, onlyIfSuccessful: false 
	}
}
}
