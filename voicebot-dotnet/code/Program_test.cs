// using System;
// using System.Net.Http;
// using System.Text;
// using System.Threading.Tasks;
// using Newtonsoft.Json;

// class Program
// {
//     static async Task Main(string[] args)
//     {
//         // Load sensitive information from the configuration file
//         string configFilePath = "appsettings.json";
//         var translatorConfig = Config.LoadConfig(configFilePath, "TranslatorSettings");
//         var languageConfig = Config.LoadConfig(configFilePath, "LanguageUnderstandingSettings");
//         var speechConfig = Config.LoadConfig(configFilePath, "SpeechSettings");
//         var mongoDBConfig = Config.LoadConfig(configFilePath, "MongoDBSettings");

//         string welcomeMsg = "Please choose a language. Say STOP to exit.";
//         await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, welcomeMsg, TextToSpeechConstants.English);

//         string response = await STT.RecognizeSpeechAsync(speechConfig.Key, speechConfig.Location, SpeechToTextConstants.English);

//         if (response.Contains("stop"))
//         {
//             await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, "Goodbye", TextToSpeechConstants.English);
//             return;
//         }

//         string sttLanguage =Helper.GetLanguage(response);

//         bool translate = sttLanguage != SpeechToTextConstants.English;

//         string prompt = "What do you want to learn about?";

//         if (translate)
//         {
//             prompt = await Translate.TranslateText(prompt, "en", sttLanguage.Split("-")[0], translatorConfig.Key, translatorConfig.Location);
//         }

//         await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, prompt, Constants.STTToTTS[sttLanguage]);

//         response = await STT.RecognizeSpeechAsync(speechConfig.Key, speechConfig.Location, sttLanguage);

//         if (translate)
//         {
//             response = await Translate.TranslateText(response, sttLanguage.Split("-")[0], "en", translatorConfig.Key, translatorConfig.Location);
//         }

//         // string topic = GetTopTopic(response, languageConfig.Endpoint, languageConfig.Key, languageConfig.CLUProjectName, languageConfig.CLUDeploymentName).ToLower();

//         // if (string.IsNullOrEmpty(topic))
//         // {
//         //     string msg = "Sorry, I didn't understand that.";
//         //     if (translate)
//         //     {
//         //         msg = Translate.TranslateText(translatorConfig.Key, translatorConfig.Location, msg, "en", sttLanguage.Split("-")[0]);
//         //     }
//         //     await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, msg, Constants.STTToTTS[sttLanguage]);
//         //     return;
//         // }

//         // string audioUrl = GetAudioURLFromMongoDB(topic, mongoDBConfig.MongoURI, mongoDBConfig.DatabaseName, mongoDBConfig.CollectionName);

//         // if (audioUrl != null)
//         // {
//         //     PlayAzureBlobAudio(audioUrl);
//         // }
//         // else
//         // {
//         //     string msg = "Sorry, I don't know about that topic.";
//         //     if (translate)
//         //     {
//         //         msg = await Translate.TranslateText(translatorConfig.Key, translatorConfig.Location, msg, "en", sttLanguage.Split("-")[0]);
//         //     }
//         //     await TTS.SynthesizeSpeechAsync(speechConfig.Key, speechConfig.Location, msg, Constants.STTToTTS[sttLanguage]);
//         // }
//     }

// }
