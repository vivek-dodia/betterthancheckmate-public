me and my girl tried this app called checkmate but somehow could not figure out how they calculate their compatibility score, so i just made my own to see and get the accurate results based on math and not some bs algorithm made to be used to match frats lol

https://stanforddaily.com/2023/04/09/opinion-yu-checkmate-and-ai-reality/

### sql query to create the db with the specific schema that i have mapped to the python code that will push to the db

```
CREATE TABLE compatibility_results (
    Date TIMESTAMP,
    overall_compatibility NUMERIC,
    career_compatibility NUMERIC,
    love_compatibility NUMERIC,
    feelings_compatibility NUMERIC
);
```


#### connection to supabase api to push the data directly to table
once the table/schema is created in your db, grab those precious keys and paste them in the code below

```
    url: str = "https://random.supabase.co"
    key: str = "key"
    supabase: Client = create_client(url, key)
```

### Sample output

```
PS C:\Users\Vivek\Documents\betterthancheckmate> python.exe .\betterthancheckmate.py
User 1, please answer the following questions:
Would you relocate for a significant other? (1 being not willing, 10 being very willing)
Rate from 1 to 10: 9
Rate how significantly your relationship with your parents has influenced your life. (1 being not at all, 10 being significantly)
Rate from 1 to 10: 7
To what extent do past experiences influence your current decisions? (1 being not at all, 10 being completely)
Rate from 1 to 10: 8
How much do cultural differences matter to you in a relationship? (1 being not at all, 10 being a great deal)
Rate from 1 to 10: 5
How deeply do you regret certain aspects of your life? none (1) everything (10)
Rate from 1 to 10: 8
To what extent do you consider yourself empathetic? (1 being not empathetic, 10 being highly empathetic)
Rate from 1 to 10: 7
How do you feel about your partner taking a career break for family or personal reasons? (1 being uncomfortable, 10 being supportive)
Rate from 1 to 10: 10
To what extent are you willing to make career sacrifices to support your partner's career? (1 being not willing, 10 being very willing)
Rate from 1 to 10: 7
How essential is communication in resolving conflicts for you? (1 being not essential, 10 being very essential)
Rate from 1 to 10: 10
How do you typically handle not achieving something despite hard work? (1 being easily discouraged, 10 being resilient)
Rate from 1 to 10: 2

User 2, please answer the same questions:
Would you relocate for a significant other? (1 being not willing, 10 being very willing)
Rate from 1 to 10: 2
Rate how significantly your relationship with your parents has influenced your life. (1 being not at all, 10 being significantly)
Rate from 1 to 10: 4
To what extent do past experiences influence your current decisions? (1 being not at all, 10 being completely)
Rate from 1 to 10: 4
How much do cultural differences matter to you in a relationship? (1 being not at all, 10 being a great deal)
Rate from 1 to 10: 8
How deeply do you regret certain aspects of your life? none (1) everything (10)
Rate from 1 to 10: 7
To what extent do you consider yourself empathetic? (1 being not empathetic, 10 being highly empathetic)
Rate from 1 to 10: 4
How do you feel about your partner taking a career break for family or personal reasons? (1 being uncomfortable, 10 being supportive)
Rate from 1 to 10: 5
To what extent are you willing to make career sacrifices to support your partner's career? (1 being not willing, 10 being very willing)
Rate from 1 to 10: 6
How essential is communication in resolving conflicts for you? (1 being not essential, 10 being very essential)
Rate from 1 to 10: 8
How do you typically handle not achieving something despite hard work? (1 being easily discouraged, 10 being resilient)
Rate from 1 to 10: 8

Your overall compatibility score is: 61.11%
Compatibility in career: 55.56%
Compatibility in love: 55.56%
Compatibility in feelings: 69.44%
2024-01-03 22:16:35,035:INFO - HTTP Request: POST https://random.supabase.co/rest/v1/compatibility_results "HTTP/1.1 201 Created"
Results saved successfully.
PS C:\Users\Vivek\Documents\betterthancheckmate>
```