using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.Text;
// using MongoDB.Driver;
// using MongoDB.Bson;


public class btManager : MonoBehaviour
{
    
    // Start is called before the first frame update
    void Start()
    {   
        /*
        var client = new MongoClient("mongodb+srv://namets:jqX8Vk3tahkPNbsm@brace.nourj.mongodb.net/?retryWrites=true&w=majority");
        client.StartSession();
        var collections = client.GetDatabase("brace").ListCollectionNames();
        Debug.Log("Collections found: " + collections);
        */
        var data = new
                {                
                breath = 3,
                pressure = 1,
                worn = 1
                };
        string d = "{breath = 3, pressure = 1, worn = 1}";        
        string newdata = Stringify(d); 

        Debug.Log(d);
        Upload(d);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public string Stringify(object data){
        return JsonUtility.ToJson(data);
    }

    IEnumerator Upload(string profile)
    {
       
        string url = "mongodb+srv://namets:jqX8Vk3tahkPNbsm@brace.nourj.mongodb.net/?retryWrites=true&w=majority";
        using (UnityWebRequest request = new UnityWebRequest(url, "POST"))
        {
            request.SetRequestHeader("Content-Type","application/json");
            byte[] bodyraw = System.Text.UTF8Encoding.UTF8.GetBytes(profile);
            request.uploadHandler = new UploadHandlerRaw(bodyraw);
            request.downloadHandler = new DownloadHandlerBuffer();  
            yield return request.SendWebRequest();

            Debug.Log(request.downloadHandler.ToString());

            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(request.error);
            }
            else
            {
                Debug.Log("Form upload complete!");
            }
        }
    }
    

  
}
