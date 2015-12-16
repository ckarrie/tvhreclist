What is it?
=====================================================================

Creates a List of TVHeadend-Recordings with
Title / Subtitle / Filename mapping
and saves it as a CSV file.


How to use?
=====================================================================

create venv
run pip install -e requirements.txt
set DVR_LOG_DIR, LANG_CODE and OUT_FN in ../src/tvhreclist/dvrreclist.py
copy files from ~/.hts/config/dvr/logs to ../src/tvhreclist/dvr_log
run python ../src/tvhreclist/dvrreclist.py

How to sort?
=====================================================================

Use Libreoffice Calc to import your CSV,
select the first row then make it sortable by Data > Filter > AutoFilter