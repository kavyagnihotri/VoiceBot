using System;
using System.Web;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Intent;

// See https://aka.ms/new-console-template for more information
namespace audioBox
{
    class Program
    {
        static void Main(string[] args)
        {
            // read text from mic


            // read intent
        }

        private static async Task<string> GetTextfromMicAsync()
        {
            var config = SpeechConfig.FromSubscription("key", "region");
            using (var recognizer = new IntentRecognizer(config))
            {
                Console.WriteLine("Speak now.. ");
                var result = await recognizer.RecognizeOnceAsync();
                if(result.Reason == ResultReason.RecognizedSpeech)
                {
                    return result.Text;
                }
                else
                {
                    return "Speech could not be understood.";
                }
            }
        }

        private static async Task<string> GetIntents(string predicationKey, string predicationEndpoint, string appID, string text)
        {
            var client = new HttpClient();
            var queryString = HttpUtility.ParseQueryString(string.Empty);
            try
            {
                client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", predicationKey);
                queryString["query"] = text;
                var preEndPointUri = String.Format("{0}Luis/prediction/v3.0/apps/{1}/slots/production/predict?{2}", predicationEndpoint, appID, quer);
            }


        }
    }
}

