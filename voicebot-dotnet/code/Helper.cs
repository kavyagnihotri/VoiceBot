using System;
using System.Net.Http;
using System.Threading.Tasks;
using MongoDB.Driver;

class Helper
{
    // public static async Task<string> GetAudioURLFromMongoDB(string topic, string mongoUri, string mongoDb, string mongoCollection)
    // {
    //     var client = new MongoClient(mongoUri);
    //     var database = client.GetDatabase(mongoDb);
    //     var collection = database.GetCollection<BsonDocument>(mongoCollection);

    //     var filter = Builders<BsonDocument>.Filter.Eq("name", topic);
    //     var document = await collection.Find(filter).FirstOrDefaultAsync();

    //     if (document != null)
    //     {
    //         Console.WriteLine(document);
    //         return document.GetValue("url").AsString;
    //     }
    //     else
    //     {
    //         return null;
    //     }
    // }

    public static void PlayAzureBlobAudio(string audioUrl)
    {
        try
        {
            using (HttpClient client = new HttpClient())
            {
                var response = client.GetAsync(audioUrl).Result;

                if (response.IsSuccessStatusCode)
                {
                    var audioData = response.Content.ReadAsByteArrayAsync().Result;
                    // Process the audio data as needed
                    // For example, you can play audio using external libraries or built-in APIs.
                    
                }
                else
                {
                    Console.WriteLine($"Failed to fetch audio from {audioUrl}. Status code: {response.StatusCode}");
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e}");
        }
    }

    public static string GetLanguage(string query)
    {
        foreach (var language in Constants.Languages)
        {
            if (query.Contains(language.Key))
            {
                return language.Value;
            }
        }
        return SpeechToTextConstants.Hindi; 
    }
}
