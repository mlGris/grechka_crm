"""v3

Revision ID: f0c235bfaa02
Revises: ef59fbb85a62
Create Date: 2024-12-24 00:58:56.182777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0c235bfaa02'
down_revision: Union[str, None] = 'ef59fbb85a62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects_history', sa.Column('id', sa.Uuid(), nullable=False))
    op.drop_column('projects_history', 'project_id')
    op.add_column('subscriptions_history', sa.Column('id', sa.Uuid(), nullable=False))
    op.drop_column('subscriptions_history', 'subscription_id')
    op.add_column('us_to_pr_history', sa.Column('id', sa.Uuid(), nullable=False))
    op.drop_column('us_to_pr_history', 'relation_id')
    op.add_column('users_history', sa.Column('id', sa.Uuid(), nullable=False))
    op.drop_column('users_history', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_history', sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('users_history', 'id')
    op.add_column('us_to_pr_history', sa.Column('relation_id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('us_to_pr_history', 'id')
    op.add_column('subscriptions_history', sa.Column('subscription_id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('subscriptions_history', 'id')
    op.add_column('projects_history', sa.Column('project_id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('projects_history', 'id')
    # ### end Alembic commands ###