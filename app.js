//progress bar 
import React, { Component } from 'react';
// import ProgressBar from './ProgressBar';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      progress: 0
    };
  }

  increase = () => {
    if (this.state.progress < 100) {
      this.setState({ progress: this.state.progress + 10 });
    }
  }

  decrease = () => {
    if (this.state.progress > 0) {
      this.setState({ progress: this.state.progress - 10 });
    }
  }

  render() {
    return (
      <div>
        <h2>Custom Progress Bar</h2>
        <ProgressBar value={this.state.progress} />
        <br />
        <button onClick={this.increase}>Increase</button>
        <button onClick={this.decrease}>Decrease</button>
        <p>Progress: {this.state.progress}%</p>
      </div>
    );
  }
}





// props validation 
import React, { Component } from 'react';
import StudentCard from './StudentCard';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Props Validation Demo</h1>

        <StudentCard name="Abhi" age={21} course="MSc CS" />
        <StudentCard name="Raj" age={20} />
        <StudentCard name="Sam" age="twenty" course="BCA" />

      </div>
    );
  }
}
