import './App.css';

function App() {
  return (
    <div className="App">
      Hi
    </div>
  );
}

export default App;

// import React, { useState } from 'react';
// import AudioRecorder from './AudioRecorder';
// import ResultDisplay from './ResultDisplay';
// import axios from 'axios';

// function App() {
//   const [result, setResult] = useState('');

//   const handleRecordingComplete = (audioBlob) => {
//     // Send the audioBlob to the Flask server
//     const formData = new FormData();
//     formData.append('audio', audioBlob);

//     axios.post('/process_audio', formData)
//       .then((response) => {
//         setResult(response.data.result);
//       })
//       .catch((error) => {
//         console.error(error);
//       });
//   };

//   return (
//     <div className="App">
//       <h1>Audio Processing App</h1>
//       <AudioRecorder onRecordingComplete={handleRecordingComplete} />
//       <ResultDisplay result={result} />
//     </div>
//   );
// }

// export default App;
