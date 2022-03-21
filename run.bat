rem pytest -v -m "sanity" --html=Reports\report.html testCases
pytest -v -m "function" --html=Reports\report_chrome.html testCases --browser chrome
pytest -v -m "function" --html=Reports\report_firefox.html testCases --browser firefox
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser firefox
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser opera
rem pytest -v -m "sanity or function" --html=Reports\report_opera.html testCases --browser opera