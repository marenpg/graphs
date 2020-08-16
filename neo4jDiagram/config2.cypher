(CREATE
(`0` :AgeCategory {description : 'string', name : 'string', id : 'string', ontology: 'string'}), 
(`1` :Analysis {shrinkageCorrection : 'string', name : 'string', dataType : 'string', id : 'string', numberOfAnimals: 'string'}), 
(`2` :BamsRegion {description : 'string', id : 'string', name: 'string'}),  
(`3` :BrainRegion {name : 'string', id: 'string'}),  
(`4` :Calculation {description : 'string', id: 'string'}), 
(`5` :CellClass {ontology : 'string', name : 'string', id: 'string'}), 
(`6` :CellDescription {description : 'string', id : 'string', iri: 'string'}),  
(`7` :CellGroup {ontology : 'string', name : 'string', id: 'string'}), 
(`8` :CellMorphology {totalArborLength : 'string', maxEuclideanDistance : 'string', overallDepth : 'string', fractalDimension : 'string', physicalIntegrity : 'string', morphologicalAttributes : 'string', neuromorphoId : 'string', overallWidth : 'string', averageBifurcationAngleRemote : 'string', averageContraction : 'string', structuralDomains : 'string', averageRalls : 'string', partitionAsymmetry : 'string', overallHeight : 'string', maxPathDistance : 'string', averageBifurcationAngleLocal : 'string', somaSurface : 'string', averageBranchDiameter : 'string', originalFormat : 'string', totalFragmentation : 'string', totalArborVolume : 'string', maxBranchOrder : 'string', numberOfBranches : 'string', numberOfBifurcations : 'string', totalArborSurface : 'string', numberOfStems : 'string', name : 'string', id: 'string'}),
(`9` :CellPhenotype {id : 'string', name : 'string', ontology: 'string'}), 
(`10` :CellPhenotypeCategory {name : 'string', id: 'string'}),  
(`11` :CellType {id : 'string', name : 'string', ontology: 'string'}), 
(`12` :CellularRegion {name : 'string', ontology : 'string', id: 'string'}), 
(`13` :ConsideredPaper {firstAuthor : 'string', id : 'string', title : 'string', publishedYear : 'string', isIncluded: 'string'}), 
(`14` :Distribution {sectionSampling : 'string', finalEstimateBasis : 'string', distribution : 'string', distributionDimensions : 'string', samplingFraction : 'string', analysisTypePrimary : 'string', subsectionalSampling : 'string', id : 'string', name : 'string', analysisTypeSecondary: 'string'}),  
(`15` :ElectronMicroscopeDetail {magnification : 'string', gridType : 'string', name : 'string', id: 'string'}), 
(`16` :ExclusionReason {reason: 'string'}),  
(`17` :Experiment {id : 'string', animalStatus : 'string', name : 'string', weightLowerLimit : 'string', weightUpperLimit : 'string', ageLowerLimit : 'string', ageUpperLimit: 'string'}),  
(`18` :IntroductionTiming {name : 'string', id: 'string'}),  
(`19` :IntroductionType {name : 'string', id: 'string'}),  
(`20` :LightFluorescenceMicroscopeDetail{refractionMedium : 'string', objectiveLens : 'string', totalMagnification : 'string', name : 'string', id : 'string', numericalAperature : 'string', opticalSliceSize: 'string'}), 
(`21` :Microscope {id : 'string', type : 'string', ontology: 'string'}), 
(`22` :NeuralStructure {id : 'string', name : 'string', ontology: 'string'}), 
(`23` :Neuromorpho {href : 'string', base64 : 'string', archive : 'string', id: 'string'}),  
(`24` :Nomenclature {doi : 'string', authors : 'string', id : 'string', published : 'string', version : 'string', name : 'string', preferred : 'string', publicationType: 'string'}), 
(`25` :Quantitation {finalEstimateBasis : 'string', sectionSampling : 'string', estimateExtraction : 'string', density : 'string', volumetricDensity : 'string', id : 'string', densityUnit : 'string', name : 'string', subsectionalSampling : 'string', densitySD : 'string', number : 'string', numberSD : 'string', samplingFraction : 'string', originalExtent : 'string', estimateRelevance: 'string'}), 
(`26` :RegionRecord {id : 'string', specificity : 'string', illustration : 'string', isAtlasRegion : 'string', documentationScore : 'string', coverage : 'string', regionalCharacteristics : 'string', annotatedImages : 'string', collectorsComment : 'string', parcellationScheme : 'string', numberOfOriginalRegions : 'string', originalRegionRetained : 'string', serialSections : 'string', semanticDescription : 'string', name : 'string', atlasCoordinates: 'string'}), 
(`27` :RegionZone {ontology : 'string', name : 'string', id: 'string'}), 
(`28` :Reporter {type : 'string', originSpecie : 'string', name : 'string', id : 'string', rrid : 'string', comment: 'string'}),  
(`29` :ReporterIncubation {order : 'string', id : 'string', time : 'string', concentration: 'string'}), 
(`30` :ReporterLabel {name : 'string', id: 'string'}),  
(`31` :ReporterTarget {id : 'string', phenotype: 'string'}), 
(`32` :SectioningDetail {sectionThickness : 'string', id : 'string', sectionOrientation: 'string'}), 
(`33` :SectioningInstrument {name : 'string', id: 'string'}),  
(`34` :Sex {name : 'string', ontology : 'string', id: 'string'}), 
(`35` :Software {rrid : 'string', name : 'string', id: 'string'}), 
(`36` :Source {type : 'string', sourceName : 'string', title : 'string', id : 'string', insertedDate : 'string', rawDataAvailable : 'string', publicationYear: 'string'}), 
(`37` :SourceOrigin {identifier : 'string', name : 'string', id: 'string'}),  
(`38` :Specie {name : 'string', id: 'string'}),  
(`39` :Specimen {form : 'string', order : 'string', name : 'string', id: 'string'}),  
(`40` :StereologyDetail {coefficientOfError : 'string', identificationFeature : 'string', probe : 'string', anyExceptProbe : 'string', areaSubfraction : 'string', investigatedSections : 'string', name : 'string', id : 'string', heightSubfraction : 'string', volumeUnit : 'string', estimatedVolume : 'string', countedObjects : 'string', disectorHeight : 'string', investigatedFields: 'string'}), 
(`41` :Strain {id : 'string', name : 'string', ontology: 'string'}), 
(`42` :Substrain {name : 'string', id: 'string'}),  
(`43` :TransgenicLine {name : 'string', id : 'string', RRID: 'string'}), 
(`44` :TreatmentPurpose {name : 'string', id: 'string'}),  
(`45` :VisualizationProtocol {ontology : 'string', name : 'string', id: 'string'}), 