function ProgressBar(props) {
  
  const trackStyle = {
    width: '100%',
    backgroundColor: 'lightgrey',
    borderRadius: '10px',
    height: '30px',
    border: '1px solid black'
  };

  const fillStyle = {
    width: props.value + '%',
    backgroundColor: 'green',
    height: '30px',
    borderRadius: '10px',
    textAlign: 'center',
    color: 'white',
    lineHeight: '30px'
  };

  return (
    <div style={trackStyle}>
      <div style={fillStyle}>
        {props.value}%
      </div>
    </div>
  );
}

export default ProgressBar;