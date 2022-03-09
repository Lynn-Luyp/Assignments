function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
hx = 1./(1+e.^(-1.*(X*theta)));
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

J = -1/m.*(y'*log(hx)+(1-y)'*log(1-hx))+sum(lambda/(2*m)*theta(:)(2:numel(theta)).^2);
grad(1) = 1/m*(hx-y)'*X(:,1);
grad(2:size(theta)) = 1/m*(hx-y)'*X(:,2:size(theta))+(lambda/m.*theta(2:size(theta)))';


% =============================================================

end
