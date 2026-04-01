import PropTypes from 'prop-types';

function StudentCard(props) {
  return (
    <div style={{ border: '1px solid black', padding: '10px', margin: '10px' }}>
      <h2>Student Details</h2>
      <p>Name: {props.name}</p>
      <p>Age: {props.age}</p>
      <p>Course: {props.course}</p>
    </div>
  );
}

StudentCard.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
  course: PropTypes.string
};

StudentCard.defaultProps = {
  course: 'Not Assigned'
};

export default StudentCard;