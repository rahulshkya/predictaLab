import React, { useState } from "react";

export default function Form(){
    let [fullname,setfullname]=useState("rahulshakya");

    function handleChange(e){
       console.log(e.target.value);
       setfullname(e.target.value);
       console.log(fullname);
    }
    return (
        <form>
            <input type="text" placeholder="Enter your name" value={fullname} onChange={handleChange}/>
            <button type="submit" onClick={handleChange}>Submit</button>
        </form>
    )
}