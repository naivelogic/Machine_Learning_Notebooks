PROC IMPORT OUT= WORK.train
            DATAFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/df_train5v3.csv" 
            DBMS=CSV REPLACE;
     GETNAMES=YES;
     DATAROW=2; 
RUN;
PROC IMPORT OUT= WORK.test
            DATAFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/df_test5v3.csv" 
            DBMS=CSV REPLACE;
     GETNAMES=YES;
     DATAROW=2; 
RUN;


data train; set train;

*if full_sq > 280 then delete;
** log tansformation;
price_log = log(price_doc);
full_sq_log = log(full_sq+1);
life_sq_log = log(life_sq+1);
catering_km_log = log(catering_km);
zd_vokzalykm_log = log(zd_vokzaly_avto_km+1);

run;

data test; set test; 
price_doc = . ; 
price_log=.; 

run;

data bank; set train test;

** log tansformation;

price_log = log(price_doc);
full_sq_log = log(full_sq+1);
life_sq_log = log(life_sq+1);
catering_km_log = log(catering_km);
zd_vokzalykm_log = log(zd_vokzaly_avto_km+1);

run;


data TrainData TestData; set train; if ranuni(1)<2/3 then output TrainData; else output TestData; run;



***************************************************************
***************************************************************
					L A S S O   (A D A P T I V E)
***************************************************************
***************************************************************
;


***
RMSE: 0.46545
Adj R2: 0.3903
SBC: -24228
AIC: -8760.64877
CVEX PRESS	0.22295
;

ods graphics on;
title "Selection Method LASSO (adaptive) Using CVExternal";                                                                                                                                                                                                         
proc glmselect data=TrainData testdata=TestData seed=123 plots(stepaxis=normb)=all ;
*partition fraction(validate=.3);

class ecology sub_area state_cat num_room product_type_investment;
	model price_log = full_sq num_room zd_vokzalykm_log ecology product_type_investment
	full_sq*sub_area  full_sq*state_cat sub_area num_room*sport_objects_raion  
       / selection=lasso(adaptive stop=none choose=cvex) cvmethod=split(10) cvDetails=all;
       *selection=lasso(stop=none choose=CV) cvmethod=random(10);
       output out = lasso_model_output  p=predict r=r;
run;                                                                                                                                                                                                                     
quit;                                                                                                                                                                                                                    
ods graphics off;

  proc export data=lasso_model_output dbms=csv 
 	OUTFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/lasso_result.csv" replace; 
 run;



ods graphics on;
proc glm data = bank plots=all PLOTS(MAXPOINTS= 25471);
class ecology sub_area state_cat num_room product_type_investment;
	model price_log = full_sq num_room zd_vokzalykm_log ecology product_type_investment
	full_sq*sub_area  full_sq*state_cat sub_area num_room*sport_objects_raion  / tolerance solution clparm  ;
	output out = lasso_final_model p=predict PRESS=CSVPress r=r;
run;quit;ods graphics off;


proc sql;
select distinct id into :idlist separated by ',' 
from test;
quit;
** Prediction on Test;
data lasso_results;
	set lasso_final_model;
	where id in (&idlist.);
	price_doc = exp(predict);
	keep id price_doc;
	run;


 proc export data=lasso_results dbms=csv 
 	OUTFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/lasso_submission.csv" replace; 
 run;










***************************************************************
***************************************************************
E L A S T I C      N E T
***************************************************************
***************************************************************
;





ods graphics on;
proc glmselect data=TrainData testdata=TestData seed=123 plots(stepaxis=normb)=all ;
*partition fraction(validate=.3);
class ecology sub_area state_cat product_type_investment build_decade bigmarket
culture_top25 MonthYear school_top20_raison ;
	model price_log = full_sq zd_vokzalykm_log num_room full_sq*num_room male_female_rate workers_perc culture_top25*bigmarket
	male_female_rate*bigmarket culture_top25*male_female_rate state_cat*male_female_rate school_top20_raison bigmarket*state_cat
	num_room*sport_objects_raion full_sq*sub_area ecology build_decade*state_cat bigmarket cafe_count_5000_price_1500 
	num_room*state_cat state_cat product_type_investment raion_popul*full_sq MonthYear market_count_5000 culture_top25
/selection=elasticnet(L2=0.001 stop=none choose=cvex) cvmethod=split(10) stb;
*selection=elasticnet(L2=0.01 stop=none choose=cvex) cvmethod=split(10) stb;
       output out = elastic_model_output   p=predict r=r;
run;                                                                                                                                                                                                                     
quit;                                                                                                                                                                                                                    
ods graphics off;

  proc export data=elastic_model_output dbms=csv 
 	OUTFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/elastic_model_output_sbc.csv" replace; 
 run;



ods graphics on;
proc glm data = bank plots=all PLOTS(MAXPOINTS= 30000);
class ecology sub_area state_cat product_type_investment build_year num_room ;
	model price_log = full_sq_log zd_vokzalykm_log num_room product_type_investment sub_area   
	male_female_rate*state_cat num_room*sport_objects_raion full_sq_log*sub_area 
	cafe_count_5000_price_1500 build_year / tolerance solution clparm  ;
	output out = elastic_net_model p=predict PRESS=CSVPress r=r;
run;quit;ods graphics off;


proc sql;
select distinct id into :idlist separated by ',' 
from test;
quit;
** Prediction on Test;
data elastic_results;
	set elastic_net_model;
	where id in (&idlist.);
	price_doc = exp(predict);
	keep id price_doc;
	run;


 proc export data=elastic_results dbms=csv 
 	OUTFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Project 1/data/elastic_net_submission.csv" replace; 
 run;


