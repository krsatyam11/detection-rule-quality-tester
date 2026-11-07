## 1. Live Application

The Detection Rule Quality Tester is deployed as a Streamlit web application.

**Live application:** [Open Detection Rule Quality Tester](https://krsatyam11-detection-rule-quality-tester-app-lgakji.streamlit.app/)

Use the live link to open the hosted application in a web browser. The application provides the interface for importing Sigma YAML rules, loading supported log files, running detection checks, reviewing results, and exporting reports.

## 2. Deployment Platform

- **Application framework:** Streamlit
- **Hosting:** Streamlit-hosted deployment
- **Application entry point:** `app.py`
- **Dependency file:** `requirements.txt`

The public application URL uses the `streamlit.app` domain. The exact repository, branch, and deployment configuration should be checked in the Streamlit deployment settings rather than assumed from the public URL.

## 3. Expected Repository Structure

The deployment repository should contain the application entry point and its dependencies. Based on the documented project structure, the relevant files are:

```text
Detection-Rule-Quality-Tester/
│
├── app.py
├── core/
│   ├── rule_parser.py
│   ├── sigma_conditions.py
│   └── detection_engine.py
├── modules/
│   ├── dashboard.py
│   ├── rule_manager.py
│   ├── log_analyzer.py
│   ├── execution_engine.py
│   ├── detection_results.py
│   └── export_reports.py
├── requirements.txt
├── README.md
├── report.md
└── deployment.md
```

This is the structure described in the project documentation. If the actual repository has additional files or different module names, use the repository's current structure.

## 4. Deployment Configuration

When configuring or checking the Streamlit deployment, use the following expected settings:

| Setting | Expected value |
|---|---|
| Main file | `app.py` |
| Dependencies | `requirements.txt` |
| Framework | Streamlit |
| Python packages | Listed in `requirements.txt` |

The selected repository and branch depend on the configuration used for the existing deployment. Confirm these values in the deployment dashboard.

## 5. Deploying the Project

For a new deployment or to recreate the deployment:

1. Push the project files to a GitHub repository.
2. Confirm that `app.py` is present in the repository root, or identify its correct relative path.
3. Confirm that `requirements.txt` lists every package required by the application.
4. Open [Streamlit Community Cloud](https://share.streamlit.io/).
5. Sign in and choose the option to create or deploy an app.
6. Select the GitHub repository and the required branch.
7. Set the application file path to `app.py`.
8. Start the deployment.
9. Open the generated application URL and check the main application workflow.

The steps above describe the standard deployment workflow. They do not assert the exact repository or branch currently connected to the published application.

## 6. Updating the Deployed Application

For a Git-based deployment, updates are generally made through the connected repository:

1. Make the required changes locally.
2. Test the application locally.
3. Commit and push the changes to the branch connected to the deployment.
4. Allow Streamlit to rebuild and restart the application.
5. Open the live URL and verify the updated functionality.

If the deployment does not update, check the deployment logs and confirm that the correct repository and branch were updated.

## 7. Dependency Management

Keep all required Python packages in `requirements.txt`. When adding or upgrading a package:

1. Update `requirements.txt`.
2. Install the updated dependencies locally.
3. Run the application and test the affected features.
4. Commit and push the dependency changes.
5. Check the deployment logs for installation errors.

Avoid relying on packages that are installed only on the local machine.

## 8. File Handling and Security Considerations

The application is designed for testing detection rules against user-provided log files. Security logs may contain sensitive information, including usernames, IP addresses, hostnames, process details, and authentication records.

- Use sanitized or authorized log data when testing through the hosted application.
- Do not upload confidential production logs unless the data-handling arrangements have been reviewed and approved.
- Do not place passwords, API keys, or other secrets directly in source files or commit them to Git.
- If the application requires secrets in the future, use the platform's secrets management feature.
- The hosted application should be treated as a testing interface, not as a production SIEM or continuous monitoring service.

The local workflow and the hosted workflow may have different data-handling implications. Review the hosting platform's current terms and configuration before using sensitive data.

## 9. Post-Deployment Verification

After deployment, perform a basic check of the main workflow:

- [ ] The application opens without an error.
- [ ] The dashboard and navigation load.
- [ ] A Sigma YAML rule can be uploaded and processed.
- [ ] A supported log file can be uploaded and parsed.
- [ ] Detection execution completes.
- [ ] Detection results can be reviewed.
- [ ] Available CSV, JSON, and PDF exports work.

Use suitable test files for verification. Do not describe these checks as passed until they have actually been performed on the deployed application.

## 10. Useful Links

- **Live application:** [https://krsatyam11-detection-rule-quality-tester-app-lgakji.streamlit.app/](https://krsatyam11-detection-rule-quality-tester-app-lgakji.streamlit.app/)
- **Streamlit Community Cloud:** [https://share.streamlit.io/](https://share.streamlit.io/)
- **Streamlit deployment documentation:** [https://docs.streamlit.io/deploy/streamlit-community-cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)
- **Streamlit documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

**Project:** Detection Rule Quality Tester  
**Deployment type:** Streamlit web application  
**Purpose:** Testing supported Sigma detection rules against security log files.