import PcaDataExtractor as PcaEx
import PcaGraph as Pca

phenData = {}
Groups = []
Names = []

phenData = PcaEx.FindPhenData()
Groups = PcaEx.FindPhenGroups()
Names = PcaEx.GetIndividuals(True)

Pca.PlotPca(Names,Groups,phenData)
Pca.RenderGraph('Heading','x','y')
