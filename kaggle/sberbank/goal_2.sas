PROC IMPORT OUT=WORK.goal2 DATAFILE="./data/goal2_data.csv" 
		DBMS=CSV REPLACE;
	GETNAMES=YES;
	DATAROW=2;
RUN;

data goal2; set goal2;
price = price_doc;
months = months_;
run;

* visualize data and model assumptions; 
title "Visualizing the data and model of Price on Aggregated Months";
proc reg data = goal2; model  price = months; run;


* PROBLEM 3 - Autoregressoin without lag;
title "Proc Autoreg without lag including DWprob";
proc autoreg data = goal2; model  price = months / dw=1 dwprob; run;



* PROBLEM 4 - AR(1);
title "Proc Autoreg with AR(1) including DWprob";
proc autoreg data = goal2; model  price = months  / 