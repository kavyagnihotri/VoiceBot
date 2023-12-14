public static class SpeechToTextConstants
{
    public const string English = "en-IN";
    public const string Hindi = "hi-IN";
    public const string Kannada = "kn-IN";
    public const string Marathi = "mr-IN";
    public const string Bengali = "bn-IN";
    public const string Telugu = "te-IN";
    public const string Tamil = "ta-IN";
    public const string Malayalam = "ml-IN";
    public const string Gujarati = "gu-IN";
    public const string Urdu = "ur-IN";
    // public const string Punjabi = "pa-IN";
}

public static class TextToSpeechConstants
{
    public const string English = "en-IN-NeerjaNeural";
    public const string Hindi = "hi-IN-SwaraNeural";
    public const string Kannada = "kn-IN-SapnaNeural";
    public const string Marathi = "mr-IN-AarohiNeural";
    public const string Bengali = "bn-IN-TanishaaNeural";
    public const string Telugu = "te-IN-ShrutiNeural";
    public const string Tamil = "ta-IN-PallaviNeural";
    public const string Malayalam = "ml-IN-SobhanaNeural";
    public const string Gujarati = "gu-IN-DhwaniNeural";
    public const string Urdu = "ur-IN-GulNeural";
    // public const string Punjabi = "pa-IN";
}

public static class Constants
{
    public static readonly Dictionary<string, string> Languages = new Dictionary<string, string>
    {
        { "english", SpeechToTextConstants.English },
        { "hindi", SpeechToTextConstants.Hindi },
        { "kannada", SpeechToTextConstants.Kannada },
        { "marathi", SpeechToTextConstants.Marathi },
        { "bengali", SpeechToTextConstants.Bengali },
        { "telugu", SpeechToTextConstants.Telugu },
        { "tamil", SpeechToTextConstants.Tamil },
        { "malayalam", SpeechToTextConstants.Malayalam },
        { "gujarati", SpeechToTextConstants.Gujarati },
        { "urdu", SpeechToTextConstants.Urdu }
    };

    public static readonly Dictionary<string, string> STTToTTS = new Dictionary<string, string>
    {
        { SpeechToTextConstants.English, TextToSpeechConstants.English },
        { SpeechToTextConstants.Hindi, TextToSpeechConstants.Hindi },
        { SpeechToTextConstants.Kannada, TextToSpeechConstants.Kannada },
        { SpeechToTextConstants.Marathi, TextToSpeechConstants.Marathi },
        { SpeechToTextConstants.Bengali, TextToSpeechConstants.Bengali },
        { SpeechToTextConstants.Telugu, TextToSpeechConstants.Telugu },
        { SpeechToTextConstants.Tamil, TextToSpeechConstants.Tamil },
        { SpeechToTextConstants.Malayalam, TextToSpeechConstants.Malayalam },
        { SpeechToTextConstants.Gujarati, TextToSpeechConstants.Gujarati },
        { SpeechToTextConstants.Urdu, TextToSpeechConstants.Urdu }
    };
}
