import React, {useState} from "react"
import logo from './logo.svg';
import './App.css';
import { ReactSketchCanvas } from 'react-sketch-canvas'

const App = class extends React.Component {
  constructor(props) {
    super(props)
    this.canvas = React.createRef()
    this.state = {
      predicted_result : ''
    }
  }

  getResult(image) {

    fetch(`http://127.0.0.1:5000/get_ocr?image=${image}`).then(async res => {
      var result = await res.json()
      console.log(result.predicted_resilt)
      this.setState({predicted_result: result.predicted_resilt})
    }).catch(err => {
      console.log(err)
    })
  }

  render() {
    return (
      <div>
        <ReactSketchCanvas 
          ref={this.canvas}
          strokeWidth={5}
          strokeColor="black"
          style={{
            border: "1px solid black"
          }}
          width={512}
          height={512}
        />
        <button
          onClick={() => {
            this.canvas.current.exportImage("png")
              .then(data => {
                console.log(data)
                this.getResult(data)
              })
              .catch(err => {
                console.log(err)
              })
          }}
        >Get Image</button>
        <p>Predicted resut: {this.state.predicted_result}</p>
      </div>
    )
  }

}

export default App;
