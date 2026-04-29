\# SDTM VS Conversion Agent



\## 📌 Overview



This project implements a deterministic pipeline to convert raw clinical trial data into the \*\*SDTM Vital Signs (VS) domain\*\* format.



The system focuses on correctly transforming wide-format input data into standardized SDTM structure while ensuring controlled terminology compliance and data validation.



\---



\## ⚙️ How to Run



```bash

pip install -r requirements.txt

python run.py

```



\---



\## 🧠 Approach



The solution follows a modular pipeline:



\* \*\*tool\_wrapper.py\*\*



&#x20; \* Generates and executes an R script for data transformation

&#x20; \* Handles wide → long conversion using SDTM logic



\* \*\*validator.py\*\*



&#x20; \* Validates output dataset

&#x20; \* Checks:



&#x20;   \* Missing required columns

&#x20;   \* Null values in VSORRES

&#x20;   \* Invalid controlled terminology values



\* \*\*run.py\*\*



&#x20; \* Orchestrates the full pipeline

&#x20; \* Generates output and validation report



\---



\## 📊 Supported VS Tests



The system currently supports:



\* TEMP (Temperature)

\* SYSBP (Systolic Blood Pressure)

\* DIABP (Diastolic Blood Pressure)

\* PULSE (Pulse Rate)



\---



\## 📁 Output



The pipeline generates:



\* `output/vs.csv` → SDTM-compliant VS dataset

\* `output/generated.R` → R script used for transformation

\* `output/validation\_report.md` → validation summary



\---



\## ✅ Validation Checks



\* Required columns present

\* No null values in `VSORRES`

\* Valid `VSTESTCD` values (Controlled Terminology compliant)



\---



\## ⚠️ Limitations



\* Focuses on \*\*core SDTM VS variables only\*\*

\* Does not include extended fields such as:



&#x20; \* VSSTRES\*

&#x20; \* VISIT / VISITNUM

&#x20; \* VSDTC

\* Additional domains (e.g., HEIGHT, WEIGHT) can be added as extensions



\---



\## 🚀 Future Improvements



\* Add full SDTM variable support

\* Include visit/time metadata

\* Expand to additional clinical domains

\* Integrate LLM-based mapping for flexible schema handling



\---



\## 📝 Notes



\* Implemented using a \*\*deterministic approach\*\* for reliability and transparency

\* Controlled Terminology is used to ensure domain correctness

\* Validation ensures output quality before submission



\---



