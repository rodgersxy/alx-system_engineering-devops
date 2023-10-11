# 0x19. Postmortem

## Postmortem: Real Estate Web App Outage

*Timeline:*

* Issue Detected: Friday, November 12, 2023, 9:30 AM (EST)  :worried:  
**Detection Method:** A surge in customer complaints about missing property images and data inconsistencies was observed, indicating a widespread issue.
* Actions Taken:  
Initial investigation focused on the image rendering and data retrieval modules.  
**Assumption:** Suspected a server-side issue impacting data retrieval.  
**Misleading Paths:** Initial investigation considered server load and database performance issues, but evidence was inconclusive.
**Escalation:** The incident was escalated to the core development team responsible for the real estate web app.
**Resolution:** The issue was resolved by identifying a database synchronization problem. An urgent synchronization process was initiated, restoring missing property images and resolving data inconsistencies by Friday, November 12, 2023, 6:00 PM (EST).  

*Root Cause:*

**Cause:** The root cause was identified as a database synchronization failure.
**Explanation:** Data inconsistency and missing images occurred due to a synchronization glitch that prevented the retrieval of property images from the database.  

*Resolution:*  :smiley:

**Fix:** The issue was resolved by executing a manual synchronization process to update the database with missing property image data.
**Testing:** Thorough testing was conducted to verify the restoration of missing images and data consistency.

*Corrective and Preventative Measures:*

* Improvements/Fixes:  :satisfied:
```
Implement automated database synchronization checks and alerts.
Enhance database error handling to prevent similar synchronization failures.
Develop a more robust data consistency verification system.
```

* Tasks:
```
Develop and implement automated synchronization checks with alerting.
Enhance error handling for database synchronization issues.
Create a monitoring system for data consistency and image retrieval.
Document and standardize the manual synchronization procedure for future reference.
```
:thumbsup: :bowtie:

![pQ9YzVY](https://github.com/rodgersxy/alx-system_engineering-devops/assets/47353893/ea85e1e7-ddec-4982-af80-2dc4b8773cd8)

