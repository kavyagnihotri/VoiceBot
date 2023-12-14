using Microsoft.CognitiveServices.Speech;

class TTS
{
    public static async Task SynthesizeSpeechAsync(string speechKey, string speechRegion, string textToTranslate, string toLangSpeech)
    {
        var speechConfig = SpeechConfig.FromSubscription(speechKey, speechRegion);
        speechConfig.SpeechSynthesisVoiceName = toLangSpeech;

        using (var speechSynthesizer = new SpeechSynthesizer(speechConfig))
        {
            string text = textToTranslate;

            var speechSynthesisResult = await speechSynthesizer.SpeakTextAsync(text);
            if (speechSynthesisResult.Reason == ResultReason.SynthesizingAudioCompleted)
            {
                Console.WriteLine($"Speech synthesized for text: [{text}]");
            }
        }
    }
}
