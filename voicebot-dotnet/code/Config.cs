using Newtonsoft.Json.Linq;

class Config
{
    public string? Key { get; set; }
    public string? Location { get; set; }
    public string? Endpoint { get; set; }
    public string? Subscription { get; set; }
    public string? CLUProjectName { get; set; }
    public string? CLUDeploymentName { get; set; }
    public string? DatabaseName { get; set; }
    public string? MongoURI { get; set; }
    public string? CollectionName { get; set; }
    public string? Username { get; set; }
    public string? Password { get; set; }
    public string? Cluster { get; set; }

    public static Config LoadConfig(string filePath, string sectionName)
    {
        if (!File.Exists(filePath))
        {
            throw new FileNotFoundException($"Configuration file not found at '{filePath}'");
        }

        string json = File.ReadAllText(filePath);
        var config = JObject.Parse(json)?[sectionName]?.ToObject<Config>();
        if (config == null)
        {
            throw new Exception($"Failed to parse configuration for section '{sectionName}'");
        }
        return config;
    }
}
