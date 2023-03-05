import React,{useState,useEffect} from 'react'
import axios from 'axios'

function App() {
  const [data,setData] = useState([{}])

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/members").then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  },[])
  return(
    <div></div>
  )
}

export default App