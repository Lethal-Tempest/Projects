import React, { useState, useEffect, useRef } from "react";

function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);
  const lft=useRef()
  const cnt=useRef()
  const back=useRef()

  const handleBack=()=>{
    lft.current.style.right="100%"
    cnt.current.classList.toggle('hidden');
  }

  const handleHamburger=()=>{
    lft.current.style.right=0
    cnt.current.classList.toggle('hidden');
    console.log("Hamburger clicked")
  }

  const handleChange = (e) => {
    setTodo(e.target.value);
  };

  const handleAdd = () => {
    setTodos([...todos, { todo, isCompleted: false }]);
    setTodo("");
  };

  const handleOpt = (index) => {
    setTodos(
      todos.map((item, idx) =>
        idx === index ? { ...item, isCompleted: !item.isCompleted } : item
      )
    );
  };

  const handleDel = (index) => {
    setTodos(todos.filter((_, idx) => idx !== index));
  };

  const handleEdit = (index) => {
    const text = prompt("Enter your task");
    setTodos(
      todos.map((item, idx) =>
        idx === index ? { ...item, todo: text } : item
      )
    );
  };

  useEffect(() => {
    const content = localStorage.getItem("todos");
    if (content) {
      setTodos(JSON.parse(content));
      console.log("Getting",JSON.parse(content));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
    console.log("Storing",JSON.stringify(todos))
  }, [todos]);

  return (
    <>
      <div className="main h-screen w-screen flex bg-pink-100">
        <div ref={lft} className="left w-3/4 md:w-1/4 h-screen rounded-r-3xl bg-pink-300 text-violet-800 py-6 text-xl md:flex justify-center relative right-3/4 md:right-0 z-10 transition-all duration-700 md:justify-start">
          <div ref={cnt} className="w-5/6 h-full ml-10 mt-10 hidden md:block">
            <div ref={back} onClick={handleBack} className="w-10 h-10 flex justify-center items-center absolute right-0 top-0 m-5 md:hidden">
              <span className="material-symbols-outlined scale-150">
                chevron_left
              </span>
            </div>
            <span className="font-bold my-10 text-4xl">MyTodos</span>
            <ul className="my-5">
              <li className="py-3 flex items-center gap-3 cursor-pointer rounded-2xl hover:bg-pink-400 p-2 transition-all duration-300 active:bg-pink-500 hover:scale-105">
                <span className="material-symbols-outlined">add_circle</span>
                <span className="text-2xl font-semibold">Add New Day</span>
              </li>
              <li className="py-3 flex items-center gap-3 cursor-pointer rounded-2xl hover:bg-pink-400 p-2 transition-all duration-300 active:bg-pink-500 hover:scale-105">
                <span className="material-symbols-outlined">delete</span>
                <span className="text-2xl font-semibold">Delete a day</span>
              </li>
              <li className="py-3 flex items-center gap-3 cursor-pointer rounded-2xl hover:bg-pink-400 p-2 transition-all duration-300 active:bg-pink-500 hover:scale-105">
                <span className="material-symbols-outlined">edit_calendar</span>
                <span className="text-2xl font-semibold">Surf Days</span>
              </li>
              <li className="py-3 flex items-center gap-3 cursor-pointer rounded-2xl hover:bg-pink-400 p-2 transition-all duration-300 active:bg-pink-500 hover:scale-105">
                <span className="material-symbols-outlined">notifications_active</span>
                <span className="text-2xl font-semibold">Set Reminder</span>
              </li>
            </ul>
          </div>
        </div>
        <div className="right md:w-2/3 w-screen h-screen flex text-violet-800 absolute left-0 md:left-1/3 bg-pink-100">
          <div onClick={handleHamburger} className="h-12 w-12 bg-pink-300 rounded-full md:hidden flex items-center justify-center m-3 md:left-0 absolute">
            <span className="material-symbols-outlined scale-125">menu</span>
          </div>
          <div className="flex flex-col justify-evenly items-center h-full w-full">
            <div className="w-full h-fit flex flex-col justify-center items-center">
              <span className="text-xl">Your tasks here</span>
              <div className="w-full h-fit flex flex-col md:flex-row justify-center items-center">
                <input
                  onChange={handleChange}
                  value={todo}
                  type="text"
                  className="w-3/5 p-2 my-3 rounded-3xl h-3/5"
                  placeholder="Enter your task"
                />
                <button
                  onClick={handleAdd}
                  className="bg-violet-600 hover:bg-violet-800 text-pink-100 h-3/5 md:w-1/12 w-1/5 my-3 mx-3 rounded-3xl flex justify-center items-center transition-all duration-500 hover:scale-105 scale-125"
                >
                  Enter
                </button>
              </div>
            </div>
            <div className="w-full h-1/2 flex flex-col items-center justify-center">
              <span className="text-xl">Your tasks for the day</span>
              <div className="h-full w-3/4 bg-white p-4 m-5 rounded-3xl">
                <ol className="list-decimal px-5 text-lg">
                  {todos.map((item, index) => (
                    <li
                      key={index}
                      className="group hover:bg-pink-100/60 pl-2 rounded-lg cursor-pointer flex justify-between my-1"
                    >
                      <div onClick={() => handleOpt(index)} className="w-full h-full group">
                        <span className={item.isCompleted ? "line-through" : ""}>
                          {item.todo}
                        </span>
                      </div>
                      <div className="hidden group-hover:flex w-48 h-fit justify-evenly">
                        <button onClick={() => handleEdit(index)} className='bg-violet-600 text-pink-100 w-16 rounded-full active:bg-violet-800 hover:scale-105 transition-all duration-100'>
                          Edit
                        </button>
                        <button onClick={() => handleDel(index)} className='bg-violet-600 text-pink-100 w-16 rounded-full active:bg-violet-800 hover:scale-105 transition-all duration-100'>
                          Delete
                        </button>
                      </div>
                    </li>
                  ))}
                </ol>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
