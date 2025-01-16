"""
Title: api_call_automation
Author: Owen Sharpe
Description: using the NIH RePORTER API class to automate a data extraction process from the API.
"""

# import libraries
import os
import pandas as pd
from nih_reporter_api import NIHReporterAPI

# SUBJECT TO CHANGE
cases = ["ProjectNumber", "CoreProjectNumber", "Title", "Abstract", "ProjectStartDate",
                         "ProjectEndDate", "OrganizationName", "OrganizationState", "OrganizationCountry",
                         "CongressionalDistrict", "FiscalYear", "AwardAmount", "DirectCosts",
                         "IndirectCosts",  "BudgetStartDate", "ApplId","SubprojectId","FiscalYear","Organization",
         "ProjectNum",
        "ProjectNumSplit","ContactPiName","AllText","FullStudySection", "ProjectStartDate",
        "ProjectEndDate"]
