# Redux
- redux where to put api call
- you can't mutate state inside reducer. You can either use `Object.assign()` or `object spread operator`
    - https://redux.js.org/docs/basics/Reducers.html
- [Правила жизни с Редаксом – РОДИОНОВ И РАЗРАБОТКА – Medium](https://medium.com/родионов-и-разработка/правила-жизни-с-редаксом-6a95feefcf29)
- redux connect Currying
- [Thunks in Redux: The Basics – Fullstack Academy – Medium](https://medium.com/fullstack-academy/thunks-in-redux-the-basics-85e538a3fe60)
- [why redux-thunk??? - How to dispatch a Redux action with a timeout? - Stack Overflow](https://stackoverflow.com/questions/35411423/how-to-dispatch-a-redux-action-with-a-timeout/35415559#35415559)
    - [thunk - fetch example - How to handle errors in fetch() responses with Redux Thunk? - Stack Overflow](https://stackoverflow.com/questions/37078215/how-to-handle-errors-in-fetch-responses-with-redux-thunk#37099629)
- [reactjs - What is mapDispatchToProps? - Stack Overflow](https://stackoverflow.com/questions/39419237/what-is-mapdispatchtoprops#40068198)
- Google Images: `redux` `redux-flow` `redux state diagram` `react-redux` 

---

часто `connect` вызывается для компонента-контейнера(smart): 

```js
export default connect(mapStateToProps, mapDispatchToProps)(SomeContainer)
```
в render() этого контейнера вызывается компонент / несколько компонентов (dumb-component)
Это наверное более правильный варик.

Но есть иногда примеры когда конектятся сразу к компоненту в файле контейнера. 
допустим здесь: - [reactjs - What is mapDispatchToProps? - Stack Overflow](https://stackoverflow.com/questions/39419237/what-is-mapdispatchtoprops#40068198)
При этом контейнер - это просто файл, там нет описания компонента контейнера (функция или class extends Component и метод рендер)
```js
export default connect(mapStateToProps, mapDispatchToProps)(SomeComponent)
```

Короче это не суть. `connect` - это просто функция, которая подсоединяет какой-либо компонент к redux store. И также дает control over dispatching actions. Как бы юзай это как хочешь. Но по хорошему первый варик. Когда только контейнер имеет доступ к redux. А компонент отрисовывает данные-props или вызывает функции-props.

просто как я понял (хз мб это колхоз, но вроде самый топовый вопрос на SO по `mapDispatchToProps`) - что контейнер, это не обязательно react-component, sometimes is just a file в котором обьявляются mapStateToProps, mapDispatchToProps и это коннектится к dumb-component. Самого smart-component нет. Есть просто файл в папке `components/`. 

Ну первый варик более true, но наверное иногда это overhead/over-engineering.

поэтому часто можно в одном файле делать и компонент и контейнер

короче еще раз **контейнер - может быть просто файл**, в котором определяются `mapStateToProps`, `mapDispatchToProps`, `connect(...)(DumbComponent)` **Контейнер может не являться реакт-компонентом**. А `DumbComponent` уже юзает dispatch просто как обычные props-functions,  и юзает state (readonly) - как обычные `props`
- [вот тут в official redux docs так делают](https://redux.js.org/docs/basics/UsageWithReact.html)
    - [Complete Source](https://redux.js.org/docs/basics/ExampleTodoList.html)

**Жесткая отмена себя**: в каждом из таких файлов контейнеров делается `connect(...)()`, а он возвращает react-component. И он потом экспортируется.

---

Спорный момент - хранить абсолютно все в store, или давать некоторым компонентам local state

- [reactjs - I am using Redux. Should I manage controlled input state in the Redux store or use setState at the component level? - Stack Overflow](https://stackoverflow.com/questions/34952530/i-am-using-redux-should-i-manage-controlled-input-state-in-the-redux-store-or-u)

---
