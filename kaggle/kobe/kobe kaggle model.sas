PROC IMPORT OUT= kobe
            DATAFILE= "/home/philliph0/MSDS 6372 Applied Statistics/Kaggle/kobe/data/kobe_data_kaggle.csv" 
            DBMS=CSV REPLACE;
     GETNAMES=YES;
     DATAROW=2; 
RUN;

data kobe;set kobe; 
if shot_made_flag = '.' then test_flag = 1; else test_flag = 0;
run;


ods graphics on;
proc logistic data = kobe plots(only)=roc;
model shot_made_flag(ref='1') = fg_pct prior_shot_made shot_distance three_pct kobe_shot_loc 
	pts game_won /link =  glogit; 
	output out=predictions predicted = LogPred;
	run;

data submission;
set predictions;
where test_flag = 1;
if LogPred > .5 then shot_made_flag = 0;
if LogPred <= .5 then shot_made_flag = 1;
keep shot_id shot_made_flag;
rename shot_made_flag=shot_made_flag;
run;


proc print data = submission;
run;


 ** save new data;
 proc export data=submission dbms=csv 
 	OUTFILE= '/home/philliph0/MSDS 6372 Applied Statistics/Kaggle/kobe/data/submission.csv' replace; 
 run;
 