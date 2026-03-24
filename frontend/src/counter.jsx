import React from "react";
import { useState } from "react";
export default function Counter() {
  const [count, setCount] = useState(0);
   return(
    <div style={{ textAlign: 'center', margin: '20px' }}>
      <h2>Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: '10px' }}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
   )
}
