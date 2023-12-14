using Azure.Core;
using Azure.AI.Language.Conversations;

class CLU
{
    public async Task<string> GetTopEntityText(string text, string projectName, string deploymentName, string _endpoint, string _key)
    {
        var credential = new AzureKeyCredential(_key);

        var client = new ConversationAnalysisClient(new Uri(_endpoint), credential);

        var data = new
        {
            AnalysisInput = new
            {
                ConversationItem = new
                {
                    Text = text,
                    Id = "1",
                    ParticipantId = "1",
                }
            },
            Parameters = new
            {
                ProjectName = projectName,
                DeploymentName = deploymentName,
                StringIndexType = "Utf16CodeUnit",
            },
            Kind = "Conversation",
        };

        Response response = await client.AnalyzeConversationAsync(RequestContent.Create(data));

        dynamic conversationalTaskResult = response.Content.ToDynamic();
        dynamic conversationPrediction = conversationalTaskResult.Result.Prediction;

        string topEntityText = GetTopEntityTextFromPrediction(conversationPrediction.Entities);
        return topEntityText;
    }

    private string GetTopEntityTextFromPrediction(dynamic entities)
    {
        string topEntityText = string.Empty;

        foreach (dynamic entity in entities)
        {
            topEntityText = entity.Text;
            break;
        }

        return topEntityText;
    }
}
