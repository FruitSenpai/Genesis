Validity Checker:
	
	//CHECKS DATA VALIDITY
	CheckPcaValid(PathToFile)
	CheckPhenValid(PathToFile)
	CheckFamValid(PathToFile)
	CheckAdmixValid(PathToFile)
	
	//CHECKS AMOUNT OF COLOUMNS IN FILE
	CheckLineAmount(WhichLineToRead,PathToFile) 


PcaDataExtractor:
	//RETURNS DICTIONARY OF INDIVIDUAL NAME AND CORR GROUP
	FindPhenData()

	//RETURNS LIST OF ALL GROUPS
	FindPhenGroups()

	//RETURNS LIST OF ALL INDIVIDUALS(parameter defines whether the first or last name is returned)
	GetIndividuals( bool ReturnFirstName)
	
	//RETURNS EITHER A LIST or DICTIONARY OF GROUPS TO FindPhenGroups()
	checkIfUsedDic(data,Groups)
	checkIfUsedList(data,Groups)

	//WILL RETURN THE FILE PATH TO THE PCA.EVEC DATA
	FilePathEvec()
    

PcaGraph:
	//PLOTS POINTS TO SCATTER PLOT FOR ALL POINTS IN DATA SET
	//(PARAMETER 1 IS THE LIST OF INDIVIDUAL NAMES FROM pcaDataExtractor.GetIndividuals())
	//(PARAMETER 2 IS THE LIST OF GROUPS FROM pcaDataExtractor.FindPhenGroups())
	//(PARAMETER 3 IS THE DICTIONARY OF INDIVIDUAL NAME AND CORR GROUP FROM pcaDataExtractor.FindPhenData() )
	PlotPca(IndividualNameList,Groups,PhenDataDict):
	
	//MUST BE DONE AFTER PlotPca()
	//RENDERS THE GRAPH IN PYPLOT
	
	def RenderGraph(HeadingLabel,xLabel,yLabel):


CreateGraph:
no functions curently although this will be the class that handles the creation of all Graphs