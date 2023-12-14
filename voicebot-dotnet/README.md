# RaspberryPi Voicebot .Net Implementation
This directly contains the .NET or C# implementation of backend flow of a basic voicebot which has support of 11 Indian Languages. All of this is mentioned in the [report](../voicebot-report.pdf).

Fill the `appsettings.json` file and add the API Keys required to access Azure AI Services and connection to MongoDB client. 

### Known errors 
AzureKeyCredential and Response methods of Azure.Core required by the Conversational Language Model are not found in the nuget package. Likely problem could be usage of mac and vscode.
