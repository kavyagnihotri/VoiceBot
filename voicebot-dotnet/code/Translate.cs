using System.Text;
using Newtonsoft.Json;

class Translate {
    public static async Task<string> TranslateText(string textToTranslate, string fromLang, string toLang, string key, string location)
        {
            string endpoint = "https://api.cognitive.microsofttranslator.com";
            string route = $"/translate?api-version=3.0&from={fromLang}&to={toLang}";

            object[] body = new object[] { new { Text = textToTranslate } };
            var requestBody = JsonConvert.SerializeObject(body);

            using (var client = new HttpClient())
            using (var request = new HttpRequestMessage())
            {
                request.Method = HttpMethod.Post;
                request.RequestUri = new Uri(endpoint + route);
                request.Content = new StringContent(requestBody, Encoding.UTF8, "application/json");
                request.Headers.Add("Ocp-Apim-Subscription-Key", key);
                request.Headers.Add("Ocp-Apim-Subscription-Region", location);

                HttpResponseMessage response = await client.SendAsync(request).ConfigureAwait(false);
                string result = await response.Content.ReadAsStringAsync();

                if (!string.IsNullOrEmpty(result))
                {
                    dynamic json = JsonConvert.DeserializeObject(result);
                    result = json[0].translations[0].text;
                }

                if (string.IsNullOrEmpty(result))
                {
                    result = "Unable to translate text.";
                }
                
                return result;
            }
        }
}