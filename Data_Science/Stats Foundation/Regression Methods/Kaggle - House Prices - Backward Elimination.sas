****
Project: Kaggle Ames Sales Price Prediction
Created by: Phillip Hale
Teeammembers: William Arnost and Joe Jiang

Import test and train
****;

data train;  
infile "/Regression/data/train.csv" firstobs=2 dsd;  
input Id MSSubClass MSZoning $ LotFrontage LotArea Street $ Alley $ LotShape $ LandContour $ Utilities $ 
LotConfig $ LandSlope $ Neighborhood $ Condition1 $ Condition2 $ BldgType $ HouseStyle $ OverallQual
OverallCond YearBuilt YearRemodAdd RoofStyle $ RoofMatl $ Exterior1st $ Exterior2nd $ MasVnrType $ 
MasVnrArea ExterQual $ ExterCond $ Foundation $ BsmtQual $ BsmtCond $ BsmtExposure $ BsmtFinType1 $ 
BsmtFinSF1 BsmtFinType2 $ BsmtFinSF2 BsmtUnfSF TotalBsmtSF Heating $ HeatingQC $ CentralAir $ 
Electrical $ OneFlrSF TwoFlrSF LowQualFinSF GrLivArea BsmtFullBath BsmtHalfBath FullBath HalfBath BedroomAbvGr
KitchenAbvGr KitchenQual $ TotRmsAbvGrd Functional $ Fireplaces FireplaceQu $ GarageType $ GarageYrBlt
GarageFinish $ GarageCars GarageArea GarageQual $ GarageCond $ PavedDrive $ WoodDeckSF OpenPorchSF EnclosedPorch 
_3SsnPorch ScreenPorch PoolArea PoolQC $	Fence $	MiscFeature $ MiscVal $ MoSold YrSold SaleType $ SaleCondition $ SalePrice
;
run;

data test;  
infile "/Regression/data/test.csv" firstobs=2 dsd;  
input Id MSSubClass MSZoning $ LotFrontage LotArea Street $ Alley $ LotShape $ LandContour $ Utilities $ 
LotConfig $ LandSlope $ Neighborhood $ Condition1 $ Condition2 $ BldgType $ HouseStyle $ OverallQual
OverallCond YearBuilt YearRemodAdd RoofStyle $ RoofMatl $ Exterior1st $ Exterior2nd $ MasVnrType $ 
MasVnrArea ExterQual $ ExterCond $ Foundation $ BsmtQual $ BsmtCond $ BsmtExposure $ BsmtFinType1 $ 
BsmtFinSF1 BsmtFinType2 $ BsmtFinSF2 BsmtUnfSF TotalBsmtSF Heating $ HeatingQC $ CentralAir $ 
Electrical $ OneFlrSF TwoFlrSF LowQualFinSF GrLivArea BsmtFullBath BsmtHalfBath FullBath HalfBath BedroomAbvGr
KitchenAbvGr KitchenQual $ TotRmsAbvGrd Functional $ Fireplaces FireplaceQu $ GarageType $ GarageYrBlt
GarageFinish $ GarageCars GarageArea GarageQual $ GarageCond $ PavedDrive $ WoodDeckSF OpenPorchSF EnclosedPorch 
_3SsnPorch ScreenPorch PoolArea PoolQC $	Fence $	MiscFeature $ MiscVal $ MoSold YrSold SaleType $ SaleCondition $
;

** add sales price to test data set for future placement for submission predictions to kaggle;
SalePrice = .;
run;

* Create new data set for all ames data that includes both train and test data for EDA and pre-processing;
data ames;
	set train test;
	
	** 4 outliers removed houses that have sqft > 4000
	indicating from reviewing Cooks D showing high leverage.;
	if id = 524 then delete;  
	if id = 1299 then delete; 
	if id = 1183 then delete;
	if id = 692 then delete;
	
	** cleaning up NA from analysis setting empty values to the most frequent type that 
	made the most sense depending on the category or if there were many NA just set to None;
	if Exterior1st = "NA" 	then 	Exterior1st="Wd Sdng";
	if Exterior2nd="NA" 	then Exterior2nd= "Wd Shng";
	if BsmtCond = "NA" 		then 	BsmtCond="None";
	if MasVnrType="NA" 		then 	MasVnrType="None";
	if KitchenQual="NA" 	then 	KitchenQual="TA";
	if Functional="NA" 		then 	Functional="None";
	if FireplaceQu="NA" 	then 	FireplaceQu="None";
	if BsmtFinSF1="NA" 		then 	BsmtFinSF1=0;
	if BsmtFinSF2="NA"   then BsmtFinSF2=0;
	if BsmtFinType2="NA" then BsmtFinType2="None";
	if GarageType="NA" then GarageType="None";
	if BsmtQual="NA" then BsmtQual="None";
	
	if SaleType ='NA' then SaleType = 'None';
	if GarageArea="NA" then GarageArea=0;
	if BsmtExposure="NA" then BsmtExposure="None";
	if BsmtFinType1="NA" then BsmtFinType1="None";
	if GarageFinish="NA" then GarageFinish="None";
	if MSZoning="NA" then MSZoning="RL";

	
	** Data Manipulation on indicator varibles that teammate Joe 
		performed analysis that proved to have better indication rather seeing values to 0 
		a latter added others;
	if YrSold >2007 then YrSold = 2008;
	if OverallQual <3 then OverallQual =2;
 	if OverallCond <4 then OverallCond =3;
 	if Fireplaces >2 then Fireplaces =2;
 	if TotRmsAbvGrd <4 then TotRmsAbvGrd =3;
 	if TotRmsAbvGrd>10 then TotRmsAbvGrd =10;
 	if WoodDeckSF >0 then WoodDeckSF =1;
 	if OpenPorchSF >0 then OpenPorchSF =1;
 	if EnclosedPorch > 0 then EnclosedPorch =1;
 	if _3SsnPorch > 0 then _3SsnPorch =1;
 	if ScreenPorch > 0 then ScreenPorch =1;
 	if PoolArea > 0 then PoolArea =1;	
 	if Electrical 'SBrkr' then Electrical = 'Fuse';
 	if Utilities = 'NA' then Utilities = 'AllPub';
 
 	if MSSubClass = 150 then MSSubClass = 120;
	if YearBuilt <1950  then YearBuilt =1949;
	YearBuilt = floor((2010 -YearBuilt)/10);
	if BsmtUnfSF = . then BsmtUnfSF = 0; 
	if TotalBsmtSF =. then TotalBsmtSF =0;
	if FullBath >3 then FullBath =3;
	if FullBath = 0 then FullBath =1;
	if GarageYrBlt =. then GarageYrBlt = 1950;
	if GarageYrBlt =2207 then GarageYrBlt =2007;
	if GarageYrBlt <1950 then GarageYrBlt =1949; 
	GarageYrBlt = floor((2010 -GarageYrBlt)/10);
	if GarageCars =. then GarageCars =0;
	if GarageCars >3 then GarageCars =3;
	if MasVnrArea = . then MasVnrArea = 0;
	if MasVnrType = "NA" then MasVnrType = "None";
	if GarageArea =. then GarageArea =0;
	if GarageQual="NA" then GarageQual="None";
	if GarageCond="NA" then GarageCond="None";
	
	** drop colmns that have too many NA or categories with the majority of 
	one factor that the variable is just not useful;
	Drop PoolQC;
	Drop Fence; 
	Drop Alley; 
	Drop MiscFeature;
	Drop Utilities;
run;

data ames;
 set ames;
	** pre-preocessing per clients request to describe square footage by 100;
	OneFlrSF = OneFlrSF / 100;
	TwoFlrSF = TwoFlrSF / 100;
	GrLivArea = GrLivArea/100;
	LotArea = LotArea / 100;
	MasVnrArea = MasVnrArea / 100;
	GarageArea = GarageArea/100;
	WoodDeckSF = WoodDeckSF/100;
	OpenPorchSF = OpenPorchSF/100;
	EnclosedPorch = EnclosedPorch/100;
	_3SsnPorch = _3SsnPorch/100;
	ScreenPorch = ScreenPorch/100;
	PoolArea = PoolArea/100;
	
	** log transformation (most was performed during EDA);	
	logSalePrice =log(SalePrice);
	LotArea_log = log(LotArea);
	sqft_log = log(GrLivArea);
	BsmtFinSF1_log = log(BsmtFinSF1 + 1);
	GarageArea_log = log(GarageArea +1);
	poolarea_log = log(PoolArea + 1);
	TotalBsmtSF_log = log(TotalBsmtSF + 1);
	OneFlrSF_log = log(OneFlrSF + 1);
	TwoFlrSF_log = log(TwoFlrSF + 1);
	BedroomAbvGr_log  = log(BedroomAbvGr);
	TotRmsAbvGrd_log = log(TotRmsAbvGrd );
run;


** Frequency Analysis to identify NA in test for categorica;
proc freq data=ames order=freq;
   tables LotShape Condition1 Condition2 BldgType Neighborhood Exterior1st Exterior2nd  ExterCond BsmtExposure 
			BsmtFinType1 HeatingQC CentralAir Functional BsmtQual GarageFinish PavedDrive SaleCondition YrSold HouseStyle GarageType
			 BsmtFinType2 Functional OverallQual OverallCond 
   /plots=freqplot;
run;


** Multicolinarity and VIF;
 proc reg data=ames;
  model logSalePrice = sqft_log LotArea LotArea_log BsmtFinSF1 GarageArea OverallCond OverallQual Fireplaces 
	GarageCars YearBuilt  GarageYrBlt /partial  tol vif;
 run;
 ods graphics on;
 proc corr data=ames PLOTS=MATRIX PEARSON ;
  var  GarageCars GarageYrBlt YearBuilt GarageArea logSalePrice ;
run;quit;ods graphics off;

proc imstat data=ames;
   corr GarageCars GarageYrBlt YearBuilt GarageArea logSalePrice ; 
quit;

*************************************************************************************************
      ------------------------ M O D E L    S E L E C T I O N ---------------------------- 
      ------------------------ B A C K W A R D     E L I M I N A T I O N ----------------- 
*************************************************************************************************
;

ods graphics on;
proc glmselect data = ames plots=all seed=123; partition fraction(validate = 0.2 test = 0.2);
	class Neighborhood  MSZoning ExterQual Condition1 Condition2 BldgType Street LotShape LandContour LotConfig LandSlope
		ExterCond BsmtQual MasVnrType BsmtCond BsmtExposure Heating HeatingQC CentralAir Electrical KitchenQual Functional RoofStyle
		RoofMatl Exterior1st Exterior2nd Foundation BsmtFinType1	PoolArea FireplaceQu  GarageFinish GarageQual  PavedDrive HouseStyle
		SaleCondition YrSold _3SsnPorch GarageType GarageCond BsmtFinType2 SaleType MSSubClass; 

	model logSalePrice =  sqft_log LotArea_log OverallQual  OverallCond YearBuilt BsmtFinSF1  Fireplaces       
	BedroomAbvGr GarageCars  MSZoning Street LotShape Condition1 Condition2 BldgType RoofStyle KitchenAbvGr Neighborhood
	RoofMatl Exterior1st Exterior2nd MasVnrType ExterQual ExterCond BsmtQual BsmtCond BsmtExposure BsmtFinType1  Heating HeatingQC 
	CentralAir 	Electrical KitchenQual Functional FireplaceQu GarageFinish GarageQual  PavedDrive SaleCondition _3SsnPorch PoolArea 
	YrSold HouseStyle GarageType GarageCond LandContour LotConfig LandSlope  BsmtFinType2   SaleType MSSubClass 
	Foundation YearRemodAdd   GarageYrBlt GarageArea 	TotRmsAbvGrd
	/selection=backward (select =aic stop=aic choose=cv ) cvdetails = cvpress showpvalues stats=all;
	output out = backward_results_output p = Predict;
	run; quit;
ods graphics off;

ods graphics on;
proc glm data = ames plots=all;
	class Neighborhood  CentralAir;
	model logSalePrice = sqft_log LotArea_log OverallQual OverallCond BsmtFinSF1  Neighborhood Fireplaces  GarageCars      
			 CentralAir YearBuilt / tolerance solution clparm ;
	output out = backward_results_output p=predict PRESS=CSVPress;
	
run;quit;ods graphics off;

** Prediction on Test;
data backward_results;
	set backward_results_output;
	logSalePrice = Predict;
	SalePrice = exp(logSalePrice);
	keep Id SalePrice;
	where Id > 1460;
	run;
 proc export data=backward_results dbms=csv 
 	OUTFILE= "/Kaggle Project/backward_results.csv" replace; 
 run;
 
 
 ** save new data;
 proc export data=ames dbms=csv 
 	OUTFILE= "/Kaggle Project/ames_for_correlation.csv" replace; 
 run;
 
 
