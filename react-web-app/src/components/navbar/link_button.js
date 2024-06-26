import { Link } from 'react-router-dom';

const LinkButton = ({ className, to, children }) => (
  <Link to={to} className={`btn ${className}`} role="button">
    {children} // Здесь расположены дочерние элементы компонента `LinkButton` 👶
  </Link>
);

export default LinkButton;