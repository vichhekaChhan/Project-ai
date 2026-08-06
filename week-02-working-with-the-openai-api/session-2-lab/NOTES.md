1.What happens when temperature is changed from 0.2 to 1.0?
- i notice when i change 0.2 the ai give consistent answer and 1.0 the ai give more creative.
2.Why should an application not retry every API error?
- because it taking alot of resource also some api error cant be fixed.
3.Why should the API key not be stored directly in the source code?
- Main reason is for reason if it stored it source code other developer and people will see it which is not good.
4.Why does conversation history increase token usage?
- because every next prompt or message include the previous one that why previous token also increase cost.
5.What is the main advantage of streaming?
- main advantage of streaming is that it give the answer in real time and user does not have to wait for whole answer.
6.If 10,000 users use your application, what engineering problems might appear?
- AI will become slow and it will cost more or performance problem.

### Stretch Goal Completed: S2 - Save and restore a conversation
I implemented the `/save <file>` and `/load <file>` commands to allow users to persist their conversation. also allow user to interact with history chat across each session
