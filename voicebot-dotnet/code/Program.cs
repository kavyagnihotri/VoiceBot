using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    static async Task Main(string[] args)
    {
        // Load sensitive information from the configuration file
        string configFilePath = "appsettings.json";
        var translatorConfig = Config.LoadConfig(configFilePath, "TranslatorSettings");
        var languageConfig = Config.LoadConfig(configFilePath, "LanguageUnderstandingSettings");
        var speechConfig = Config.LoadConfig(configFilePath, "SpeechSettings");
        var mongoDBConfig = Config.LoadConfig(configFilePath, "MongoDBSettings");

        // CLU - Conversational Language Understanding
        string text = "How is oxygen important?";
        // string topic = new CLU.GetTopEntityText(text, languageConfig.CLUProjectName, languageConfig.CLUDeploymentName, languageConfig.Endpoint, languageConfig.Key);
        // public async Task<string> GetTopEntityText(string text, string projectName, string deploymentName, string _endpoint, string _key)


        // STT - Speech-to-Text
        // string recognizedText = await STT.RecognizeSpeechAsync(speechConfig.Key, speechConfig.Location, SpeechToTextConstants.English);
        // // Console.WriteLine($"Recognized Text: {recognizedText}");

        // // TTS - Text-to-Speech
        // await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, recognizedText, TextToSpeechConstants.English);

        

        // string textToTranslate = "abc";
        // string fromLang = "en";
        // string toLang = "hi";

        // string translatedText = await Translate.TranslateText(textToTranslate, fromLang, toLang, translatorConfig.Key, translatorConfig.Location);
        // Console.WriteLine(translatedText);
        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }

}
